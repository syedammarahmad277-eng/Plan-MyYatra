document.addEventListener("DOMContentLoaded", () => {
    const tripForm = document.getElementById("tripForm");
    const resultsSection = document.getElementById("results");
    const tripResults = document.getElementById("tripResults");

    if (!tripForm) {
        console.error("Trip form was not found.");
        return;
    }

    tripResults.addEventListener("click", (event) => {
        const themeButton = event.target.closest("[data-itinerary-theme]");

        if (!themeButton) {
            return;
        }

        const itineraryCard = themeButton.closest(".itinerary-card");

        if (!itineraryCard) {
            return;
        }

        const selectedTheme = themeButton.dataset.itineraryTheme;

        itineraryCard
            .querySelectorAll("[data-itinerary-theme]")
            .forEach((button) => {
                const isSelected =
                    button.dataset.itineraryTheme === selectedTheme;

                button.classList.toggle("is-active", isSelected);
                button.setAttribute("aria-pressed", String(isSelected));
            });

        itineraryCard.querySelector(".itinerary-list").innerHTML =
            createItinerary(
                itineraryCard.dataset.days,
                itineraryCard.dataset.destination,
                selectedTheme,
                itineraryCard.dataset.itineraryDestination
            );
    });

    tripForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const tripData = {
            from: document.getElementById("from").value.trim(),
            destination: document.getElementById("destination").value.trim(),
            days: Number(document.getElementById("days").value),
            travelers: Number(document.getElementById("travelers").value),
            budget: Number(document.getElementById("budget").value),
            transport_mode: document.getElementById("transportMode").value,
            hotel_preference: document.getElementById("hotelPreference").value
        };

        // ------------------------------------------
        // VALIDATION
        // ------------------------------------------

        if (!tripData.from || !tripData.destination) {
            showError(
                "Please enter both your starting location and destination."
            );
            return;
        }

        if (tripData.days < 1) {
            showError("Please enter at least 1 day.");
            return;
        }

        if (tripData.travelers < 1) {
            showError("Please enter at least 1 traveler.");
            return;
        }

        if (tripData.budget <= 0) {
            showError("Please enter a valid trip budget.");
            return;
        }

        // ------------------------------------------
        // LOADING
        // ------------------------------------------

        showLoading();

        try {
            const result = await planTrip(tripData);

            console.log("Travel plan received:", result);

            if (!result || result.success === false) {
                throw new Error(
                    result?.error ||
                    "Unable to create your travel plan."
                );
            }

            displayTripResult(result);

        } catch (error) {
            console.error("Trip planning failed:", error);

            showError(
                error.message ||
                "Unable to create your travel plan. Please try again."
            );
        }
    });


    // =========================================================
    // LOADING SCREEN
    // =========================================================

    function showLoading() {
        resultsSection.classList.remove("hidden");

        tripResults.innerHTML = `
            <div class="loading-box">

                <div class="loading-spinner"></div>

                <h3>Creating Your Travel Plan...</h3>

                <p>
                    Plan MyYatra is analyzing your route,
                    transport, accommodation, budget and destination.
                </p>

            </div>
        `;

        resultsSection.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    }


    // =========================================================
    // ERROR
    // =========================================================

    function showError(message) {
        resultsSection.classList.remove("hidden");

        tripResults.innerHTML = `
            <div class="error-box">

                <div class="error-icon">
                    ⚠️
                </div>

                <h3>
                    Unable to Create Your Plan
                </h3>

                <p>
                    ${escapeHTML(message)}
                </p>

                <button
                    class="primary-btn"
                    onclick="scrollToPlanner()"
                >
                    ← Try Again
                </button>

            </div>
        `;

        resultsSection.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    }


    // =========================================================
    // DISPLAY TRAVEL PLAN
    // =========================================================

    function displayTripResult(result) {

        resultsSection.classList.remove("hidden");

        const trip =
            result.trip || {};

        const route =
            result.route || {};

        const transport =
            result.transport || {};

        const destinationInfo =
            result.destination_info || {};

        const hubs =
            result.transport_hubs || {};

        const recommendation =
            transport.recommended || {};

        const options =
            transport.options || {};


        // =====================================================
        // BASIC TRIP DATA
        // =====================================================

        const destinationName =
            destinationInfo.name ||
            trip.destination ||
            "Your Destination";

        const itineraryDestination =
            trip.destination ||
            destinationName;

        const state =
            destinationInfo.state ||
            "";

        const bestSeason =
            destinationInfo.best_season ||
            "Information unavailable";

        const travelers =
            Number(trip.travelers || 1);

        const days =
            Number(trip.days || 1);

        const budget =
            Number(trip.budget || 0);


        // =====================================================
        // RECOMMENDED TRANSPORT
        // =====================================================

        const recommendedMode =
            recommendation.mode ||
            "road";

            currentRecommendedMode = recommendedMode;
        const recommendedCostObject =
            recommendation.cost ||
            {};

        let recommendedTotalCost =
            Number(
                recommendedCostObject.total_group_cost ||
                recommendedCostObject.total_vehicle_cost ||
                recommendedCostObject.total_cost ||
                recommendation.total_group_cost ||
                recommendation.total_cost ||
                0
            );

        const recommendationReason =
            recommendation.reason ||
            "Recommended based on the estimated transport cost and your trip details.";


        // =====================================================
        // HOTEL
        // =====================================================

        const hotelPrices =
            destinationInfo.hotel_prices ||
            {};

        const hotelPreference =
            trip.hotel_preference ||
            "auto";

        let selectedHotelTier =
            hotelPreference;

        if (
            hotelPreference === "auto" ||
            !hotelPrices[hotelPreference]
        ) {
            selectedHotelTier =
                getHotelTierFromBudget(
                    budget,
                    days,
                    travelers,
                    hotelPrices
                );
        }

        const hotelNightlyPrice =
            Number(
                hotelPrices[selectedHotelTier] || 0
            );

        const nights =
            Math.max(days - 1, 0);

        const rooms =
            Math.max(
                Math.ceil(travelers / 2),
                1
            );

        const hotelTotal =
            hotelNightlyPrice *
            nights *
            rooms;


        // =====================================================
        // FOOD
        // =====================================================

        const foodPerPersonDay =
            Number(
                destinationInfo.food_per_person_day || 0
            );

        const foodTotal =
            foodPerPersonDay *
            travelers *
            days;


        // =====================================================
        // LOCAL TRANSPORT
        // =====================================================

        const localTransportPerPersonDay =
            Number(
                destinationInfo.local_transport_per_person_day || 0
            );

        const isOwnCarTrip =
            String(trip.transport_mode || "")
                .toLowerCase() === "road"
            || String(recommendedMode || "")
                .toLowerCase() === "road";

        const localTransportTotal =
            isOwnCarTrip
                ? 0
                : localTransportPerPersonDay *
                    travelers *
                    days;


        // =====================================================
        // ACTIVITIES
        // =====================================================

        const activitiesPerPersonDay =
            Number(
                destinationInfo.activities_per_person_day || 0
            );

        const activitiesTotal =
            activitiesPerPersonDay *
            travelers *
            days;


        // =====================================================
        // TOTAL
        // =====================================================

        const estimatedTotal =
            recommendedTotalCost +
            hotelTotal +
            foodTotal +
            localTransportTotal +
            activitiesTotal;


        const budgetDifference =
            budget - estimatedTotal;


        // =====================================================
        // BUDGET STATUS
        // =====================================================

        let budgetStatusHTML = "";

        if (budgetDifference >= 0) {

            budgetStatusHTML = `
                <div class="budget-status budget-good">

                    <span>✓</span>

                    <div>
                        <strong>Within your budget</strong>

                        <p>
                            Approximately
                            ₹${formatNumber(budgetDifference)}
                            remaining.
                        </p>
                    </div>

                </div>
            `;

        } else {

            budgetStatusHTML = `
                <div class="budget-status budget-warning">

                    <span>!</span>

                    <div>
                        <strong>Above your budget</strong>

                        <p>
                            Approximately
                            ₹${formatNumber(
                                Math.abs(budgetDifference)
                            )}
                            over your budget.
                        </p>
                    </div>

                </div>
            `;
        }


        // =====================================================
        // FINAL HTML
        // =====================================================

        tripResults.innerHTML = `

            <div class="travel-plan">


                <!-- =================================================
                     HEADER
                ================================================= -->

                <div class="travel-plan-header">

                    <div class="destination-heading">

                        <p class="section-label">
                            ✈ YOUR TRAVEL PLAN
                        </p>

                        <h2>
                            ${escapeHTML(destinationName)}
                        </h2>

                        <p class="destination-state">
                            ${escapeHTML(state)}
                        </p>

                    </div>

                    <div class="trip-badge">
                        ✨ Plan MyYatra
                    </div>

                </div>


                <!-- =================================================
                     SUMMARY
                ================================================= -->

                <div class="trip-summary-grid">

                    <div class="summary-card">

                        <div class="summary-icon">
                            📍
                        </div>

                        <div>
                            <small>Route</small>

                            <strong>
                                ${escapeHTML(
                                    trip.from || ""
                                )}
                                →
                                ${escapeHTML(
                                    trip.destination || ""
                                )}
                            </strong>
                        </div>

                    </div>


                    <div class="summary-card">

                        <div class="summary-icon">
                            📅
                        </div>

                        <div>
                            <small>Duration</small>

                            <strong>
                                ${days} Days
                            </strong>
                        </div>

                    </div>


                    <div class="summary-card">

                        <div class="summary-icon">
                            👥
                        </div>

                        <div>
                            <small>Travelers</small>

                            <strong>
                                ${travelers}
                            </strong>
                        </div>

                    </div>


                    <div class="summary-card">

                        <div class="summary-icon">
                            💰
                        </div>

                        <div>
                            <small>Your Budget</small>

                            <strong>
                                ₹${formatNumber(budget)}
                            </strong>
                        </div>

                    </div>

                </div>


                <!-- =================================================
                     ROUTE INFORMATION
                ================================================= -->

                <div class="result-section-card result-card route-card">

                    <div class="result-section-title">

                        <div class="section-icon blue-icon">
                            🗺️
                        </div>

                        <div>

                            <h3>
                                Route Information
                            </h3>

                            <p>
                                Approximate travel distance
                            </p>

                        </div>

                    </div>


                    <div class="route-box">

                        <div class="route-location">

                            <div class="location-icon">
                                🏙️
                            </div>

                            <div>

                                <small>
                                    Starting Point
                                </small>

                                <strong>
                                    ${escapeHTML(
                                        trip.from || ""
                                    )}
                                </strong>

                            </div>

                        </div>


                        <div class="route-middle">

                            <span>
                                ${formatNumber(
                                    route.one_way_distance_km || 0
                                )} km
                            </span>

                            <div class="route-arrow">
                                ⟶
                            </div>

                        </div>


                        <div class="route-location">

                            <div class="location-icon destination-location">
                                🏔️
                            </div>

                            <div>

                                <small>
                                    Destination
                                </small>

                                <strong>
                                    ${escapeHTML(
                                        trip.destination || ""
                                    )}
                                </strong>

                            </div>

                        </div>

                    </div>


                    <div class="round-trip-box">

                        🔄

                        <span>
                            Round-trip distance
                        </span>

                        <strong>
                            ${formatNumber(
                                route.round_trip_distance_km || 0
                            )} km
                        </strong>

                    </div>

                </div>


                <!-- =================================================
                     RECOMMENDED TRANSPORT
                ================================================= -->

                <div class="result-section-card result-card recommended-card">

                    <div class="result-section-title">

                        <div class="section-icon green-icon">
                            ✨
                        </div>

                        <div>

                            <h3>
                                Recommended Transport
                            </h3>

                            <p>
                                Based on your preferences and budget
                            </p>

                        </div>

                    </div>


                    <div class="recommended-transport">

                        <div class="transport-icon-large">
                            ${getTransportIcon(
                                recommendedMode
                            )}
                        </div>

                        <div class="transport-main">

                            <div class="transport-title-row">

                                <h3>
                                    ${getTransportName(
                                        recommendedMode
                                    )}
                                </h3>

                                <span class="best-option">
                                    Best Option
                                </span>

                            </div>

                            <p>
                                ${escapeHTML(
                                    recommendationReason
                                )}
                            </p>

                        </div>

                    </div>


                    <div class="recommended-price">

                        <div>

                            <small>
                                Estimated group cost
                            </small>

                            <strong>
                                ₹${formatNumber(
                                    recommendedTotalCost
                                )}
                            </strong>

                        </div>

                        <div>

                            <small>
                                Approx. per person
                            </small>

                            <strong>
                                ₹${formatNumber(
                                    travelers > 0
                                        ? recommendedTotalCost / travelers
                                        : 0
                                )}
                            </strong>

                        </div>

                    </div>

                </div>


                <!-- =================================================
                     TRANSPORT COMPARISON
                ================================================= -->

                <div class="result-section-card result-card transport-comparison-card">

                    <div class="result-section-title">

                        <div class="section-icon purple-icon">
                            🚆
                        </div>

                        <div>

                            <h3>
                                Transport Comparison
                            </h3>

                            <p>
                                Estimated cost for your group
                            </p>

                        </div>

                    </div>


                    <div class="transport-grid">

                        ${createTransportCard(
                            "road",
                            options.road
                        )}

                        ${createTransportCard(
                            "train",
                            options.train
                        )}

                        ${createTransportCard(
                            "bus",
                            options.bus
                        )}

                        ${createTransportCard(
                            "flight",
                            options.flight
                        )}

                    </div>

                </div>


                <!-- =================================================
                     ACCOMMODATION
                ================================================= -->

                <div class="result-section-card result-card hotel-card">

                    <div class="result-section-title">

                        <div class="section-icon orange-icon">
                            🏨
                        </div>

                        <div>

                            <h3>
                                Accommodation Estimate
                            </h3>

                            <p>
                                Based on your selected preference
                            </p>

                        </div>

                    </div>


                    <div class="hotel-main">

                        <div class="hotel-image-placeholder">
                            🛏️
                        </div>

                        <div class="hotel-category">

                            <small>
                                Suggested Category
                            </small>

                            <strong>
                                ${capitalize(
                                    selectedHotelTier
                                )}
                            </strong>

                        </div>

                        <div class="hotel-price">

                            <small>
                                Approx. / night
                            </small>

                            <strong>
                                ₹${formatNumber(
                                    hotelNightlyPrice
                                )}
                            </strong>

                        </div>

                    </div>


                    <div class="hotel-details">

                        <div>
                            <small>Nights</small>
                            <strong>${nights}</strong>
                        </div>

                        <div>
                            <small>Rooms</small>
                            <strong>${rooms}</strong>
                        </div>

                        <div>
                            <small>Estimated Total</small>
                            <strong>
                                ₹${formatNumber(hotelTotal)}
                            </strong>
                        </div>

                    </div>

                </div>


                <!-- =================================================
                     BUDGET
                ================================================= -->

                <div class="result-section-card result-card budget-card">

                    <div class="result-section-title">

                        <div class="section-icon pink-icon">
                            💰
                        </div>

                        <div>

                            <h3>
                                Budget Breakdown
                            </h3>

                            <p>
                                Estimated total trip cost
                            </p>

                        </div>

                    </div>


                    <div class="budget-breakdown">

                        ${createBudgetRow(
                            "🚗",
                            "Transportation",
                            recommendedTotalCost
                        )}

                        ${createBudgetRow(
                            "🏨",
                            "Accommodation",
                            hotelTotal
                        )}

                        ${createBudgetRow(
                            "🍽️",
                            "Food",
                            foodTotal
                        )}

                        ${createBudgetRow(
                            "🚌",
                            "Local Transport",
                            localTransportTotal
                        )}

                        ${createBudgetRow(
                            "🎯",
                            "Activities",
                            activitiesTotal
                        )}

                        <div class="budget-total">

                            <span>
                                Estimated Trip Cost
                            </span>

                            <strong>
                                ₹${formatNumber(
                                    estimatedTotal
                                )}
                            </strong>

                        </div>

                    </div>


                    ${budgetStatusHTML}

                </div>


                <!-- =================================================
                     DESTINATION INFORMATION
                ================================================= -->

                <div class="result-section-card result-card destination-card">

                    <div class="result-section-title">

                        <div class="section-icon cyan-icon">
                            🏔️
                        </div>

                        <div>

                            <h3>
                                Destination Information
                            </h3>

                            <p>
                                Useful information for your journey
                            </p>

                        </div>

                    </div>


                    <div class="destination-info-grid">

                        <div class="info-box">

                            <span>
                                🌤️
                            </span>

                            <div>

                                <small>
                                    Best Season
                                </small>

                                <strong>
                                    ${escapeHTML(
                                        bestSeason
                                    )}
                                </strong>

                            </div>

                        </div>


                        <div class="info-box">

                            <span>
                                🏔️
                            </span>

                            <div>

                                <small>
                                    Destination Type
                                </small>

                                <strong>
                                    ${capitalize(
                                        destinationInfo.type ||
                                        "Travel Destination"
                                    )}
                                </strong>

                            </div>

                        </div>


                        <div class="info-box">

                            <span>
                                🚆
                            </span>

                            <div>

                                <small>
                                    Nearest Rail Hub
                                </small>

                                <strong>
                                    ${escapeHTML(
                                        hubs.rail ||
                                        "Not available"
                                    )}
                                </strong>

                            </div>

                        </div>


                        <div class="info-box">

                            <span>
                                ✈️
                            </span>

                            <div>

                                <small>
                                    Nearest Airport
                                </small>

                                <strong>
                                    ${escapeHTML(
                                        hubs.airport ||
                                        "Not available"
                                    )}
                                </strong>

                            </div>

                        </div>

                    </div>

                </div>


                <!-- =================================================
                     ITINERARY
                ================================================= -->

                <div
                    class="result-section-card result-card itinerary-card"
                    data-days="${days}"
                    data-destination="${escapeHTML(destinationName)}"
                    data-itinerary-destination="${escapeHTML(itineraryDestination)}"
                >

                    <div class="result-section-title">

                        <div class="section-icon purple-icon">
                            📅
                        </div>

                        <div>

                            <h3>
                                Suggested Itinerary
                            </h3>

                            <p>
                                Your day-by-day travel structure
                            </p>

                        </div>

                    </div>


                    <div class="itinerary-theme-picker" aria-label="Focus your itinerary">
                        <p>Choose your travel style</p>
                        <div class="itinerary-theme-options" role="group" aria-label="Itinerary themes">
                            ${createItineraryThemeButtons("balanced")}
                        </div>
                    </div>

                    <div class="itinerary-list">

                        ${createItinerary(
                            days,
                            destinationName,
                            "balanced",
                            itineraryDestination
                        )}

                    </div>

                </div>


                <!-- =================================================
                     ACTION
                ================================================= -->

                <div class="plan-actions">

                    <button
                        class="primary-btn"
                        onclick="scrollToPlanner()"
                    >
                        ✨ Plan Another Trip
                    </button>

                </div>

            </div>
        `;


        resultsSection.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    }


    // =========================================================
    // TRANSPORT CARD
    // =========================================================

    function createTransportCard(mode, data) {

        if (!data) {
            return `
                <div class="transport-option unavailable">

                    <div class="transport-option-icon">
                        ${getTransportIcon(mode)}
                    </div>

                    <h4>
                        ${getTransportName(mode)}
                    </h4>

                    <span>
                        Not available
                    </span>

                </div>
            `;
        }

        const isRoad =
            mode === "road";

        const total =
            Number(
                isRoad
                    ? (
                        data.total_vehicle_cost ||
                        data.total_group_cost ||
                        data.total_cost ||
                        0
                    )
                    : (
                        data.total_group_cost ||
                        data.total_cost ||
                        0
                    )
            );

        const perPerson =
            Number(
                isRoad
                    ? (
                        data.shared_cost_per_person ||
                        data.cost_per_person ||
                        0
                    )
                    : (
                        data.ticket_cost_per_person ||
                        data.cost_per_person ||
                        0
                    )
            );

        const isRecommended =
            mode ===
            getCurrentRecommendedMode();


        return `
            <div
                class="transport-option
                ${isRecommended ? "selected-transport" : ""}"
            >

                ${isRecommended
                    ? `
                        <span class="recommended-label">
                            Recommended
                        </span>
                    `
                    : ""
                }

                <div class="transport-option-icon">
                    ${getTransportIcon(mode)}
                </div>

                <h4>
                    ${getTransportName(mode)}
                </h4>

                <small>
                    ${isRoad
                        ? "Total vehicle"
                        : "Group tickets"}
                </small>

                <strong>
                    ₹${formatNumber(total)}
                </strong>

                <span>
                    ₹${formatNumber(perPerson)}
                    / person
                </span>

            </div>
        `;
    }


    // =========================================================
    // RECOMMENDED MODE HELPER
    // =========================================================

    let currentRecommendedMode = "road";

    function getCurrentRecommendedMode() {
        return currentRecommendedMode;
    }


    // =========================================================
    // BUDGET ROW
    // =========================================================

    function createBudgetRow(
        icon,
        name,
        amount
    ) {

        return `
            <div class="budget-row">

                <span class="budget-name">

                    <span class="budget-row-icon">
                        ${icon}
                    </span>

                    ${name}

                </span>

                <strong>
                    ₹${formatNumber(amount || 0)}
                </strong>

            </div>
        `;
    }


    // =========================================================
    // ITINERARY
    // =========================================================

    const itineraryThemes = {
        balanced: {
            label: "Balanced",
            icon: "✦",
            description: (destination) =>
                `A little of everything: discover the highlights of ${destination} at your own pace.`
        },
        culture: {
            label: "Culture",
            icon: "🏛",
            description: (destination) =>
                `Make room for the heritage, spiritual sites and local stories of ${destination}.`
        },
        adventure: {
            label: "Adventure",
            icon: "⛰",
            description: (destination) =>
                `Put active outings and memorable outdoor experiences in the spotlight in ${destination}.`
        },
        food: {
            label: "Food",
            icon: "🍴",
            description: (destination) =>
                `Explore local flavours, market lanes and relaxed café stops around ${destination}.`
        },
        nature: {
            label: "Nature",
            icon: "🌿",
            description: (destination) =>
                `Take the scenic route through the green spaces and natural highlights of ${destination}.`
        }
    };

    const itineraryThemeKeywords = {
        culture: /\b(heritage|history|historic|temple|church|monastery|museum|spiritual|cultural|aarti|palace|fort|tomb|architecture|ashram|darshan|cathedral)\b/i,
        adventure: /\b(adventure|rafting|paragliding|trek|hike|hiking|snow activities|water sports|cable car|ride|day trip|high-altitude|cycling|kayak|safari)\b/i,
        food: /\b(food|tasting|snacks|cafe|café|breakfast|culinary|street food|local flavours|market|shopping)\b/i,
        nature: /\b(nature|scenic|lakes?|lakefront|lakeside|river|riverfront|forest|garden|waterfall|birdwatching|beach|sunrise|sunset|viewpoint|picnic|promenade|hill|park|trail|outdoors?)\b/i
    };

    function createItineraryThemeButtons(activeTheme) {
        return Object.entries(itineraryThemes).map(([theme, details]) => `
            <button
                class="itinerary-theme${theme === activeTheme ? " is-active" : ""}"
                type="button"
                data-itinerary-theme="${theme}"
                aria-pressed="${theme === activeTheme}"
            >
                <span aria-hidden="true">${details.icon}</span>
                ${details.label}
            </button>
        `).join("");
    }

    function matchesItineraryTheme(idea, theme) {
        const description = `${idea.place} ${idea.activity}`;

        return idea.theme === theme ||
            itineraryThemeKeywords[theme].test(description);
    }

    function getDestinationItineraryIdeas(destination, catalogDestination) {

        const destinationKey =
            String(destination || "")
                .trim()
                .toLowerCase();

        const itineraryIdeas = {
            "rishikesh": [
                { place: "Triveni Ghat", activity: "Evening Ganga Aarti and sunset walk" },
                { place: "Lakshman Jhula", activity: "Walk the suspension bridge and café hopping" },
                { place: "Neelkanth Mahadev Temple", activity: "Temple visit and short forest trek" },
                { place: "Beatles Ashram", activity: "Meditation, yoga and heritage photography" },
                { place: "Shivpuri", activity: "White-water rafting and riverside relaxation" },
                { place: "Rajaji National Park", activity: "Nature trail and birdwatching" },
                { place: "Ram Jhula", activity: "Morning market stroll and riverside breakfast" },
                { place: "Kunjapuri Temple", activity: "Sunrise viewpoint and spiritual visit" }
            ],
            "haridwar": [
                { place: "Har Ki Pauri", activity: "Ganga dip and evening aarti" },
                { place: "Mansa Devi Temple", activity: "Cable car ride and temple visit" },
                { place: "Chandi Devi Temple", activity: "Hilltop darshan and scenic views" },
                { place: "Kankhal", activity: "Heritage walk and local food tasting" },
                { place: "Sant Sarovar", activity: "Relaxing lakeside stroll" },
                { place: "Market area", activity: "Shopping for puja items and souvenirs" }
            ],
            "shimla": [
                { place: "The Ridge", activity: "Evening stroll and local snacks" },
                { place: "Mall Road", activity: "Shopping and café stop" },
                { place: "Jakhoo Temple", activity: "Temple visit and panoramic hike" },
                { place: "Kufri", activity: "Adventure sports and snow activities" },
                { place: "Christ Church", activity: "Heritage sightseeing" },
                { place: "Annandale", activity: "Picnic and scenic walk" }
            ],
            "manali": [
                { place: "Solang Valley", activity: "Paragliding and snow adventure" },
                { place: "Old Manali", activity: "Cafe hopping and riverside walk" },
                { place: "Hadimba Temple", activity: "Temple visit and forest walk" },
                { place: "Rohtang Pass", activity: "Mountain drive and scenic photography" },
                { place: "Beas River", activity: "Picnic and relaxed riverfront time" },
                { place: "Manu Temple", activity: "Spiritual stop and local exploration" }
            ],
            "mussoorie": [
                { place: "Gun Hill", activity: "Cable car ride and sunset view" },
                { place: "Mall Road", activity: "Shopping and evening walk" },
                { place: "Kempty Falls", activity: "Waterfall dip and nature time" },
                { place: "Lal Tibba", activity: "Scenic viewpoint and photography" },
                { place: "Camel's Back Road", activity: "Sunrise walk and relaxation" },
                { place: "Cloud's End", activity: "Nature trail and quiet retreat" }
            ],
            "goa": [
                { place: "Baga Beach", activity: "Beach hopping and water sports" },
                { place: "Palolem Beach", activity: "Sunset view and calm seaside walk" },
                { place: "Fort Aguada", activity: "Historic fort visit and coastal photography" },
                { place: "Old Goa", activity: "Churches and cultural heritage walk" },
                { place: "Dudhsagar Falls", activity: "Waterfall trek and nature experience" },
                { place: "Anjuna Beach", activity: "Market browsing and relaxed beach time" }
            ],
            "mumbai": [
                { place: "Marine Drive", activity: "Sunset promenade and local snacks" },
                { place: "Gateway of India", activity: "Heritage visit and harbor walk" },
                { place: "Elephanta Caves", activity: "Island trip and history exploration" },
                { place: "Juhu Beach", activity: "Beach walk and street food" },
                { place: "Colaba Causeway", activity: "Shopping and café break" },
                { place: "Bandra Fort", activity: "Scenic viewpoint and photo stop" }
            ],
            "jaipur": [
                { place: "Hawa Mahal", activity: "Heritage viewing and photo walk" },
                { place: "Amber Fort", activity: "Elephant ride and fort exploration" },
                { place: "City Palace", activity: "Museum visit and royal architecture" },
                { place: "Jal Mahal", activity: "Lakefront photography and calm stroll" },
                { place: "Nahargarh Fort", activity: "Sunset viewpoint and evening drive" },
                { place: "Johari Bazaar", activity: "Shopping for textiles and jewelry" }
            ],
            "agra": [
                { place: "Taj Mahal", activity: "Sunrise visit and scenic photography" },
                { place: "Agra Fort", activity: "Historic fort exploration" },
                { place: "Mehtab Bagh", activity: "Riverfront sunset viewpoint" },
                { place: "Fatehpur Sikri", activity: "Day trip and monument walk" },
                { place: "Itimad-ud-Daulah", activity: "Quiet heritage visit" },
                { place: "Sikandra", activity: "Akbar's tomb sightseeing" }
            ],
            "darjeeling": [
                { place: "Tiger Hill", activity: "Sunrise view and photography" },
                { place: "Batasia Loop", activity: "Scenic viewpoint and short sightseeing" },
                { place: "Tea Gardens", activity: "Tea tasting and plantation walk" },
                { place: "Ghoom Monastery", activity: "Cultural visit and quiet time" },
                { place: "Mall Road", activity: "Evening stroll and local shopping" },
                { place: "Padmaja Naidu Zoo", activity: "Wildlife visit and relaxed walk" }
            ],
            "gangtok": [
                { place: "MG Marg", activity: "Evening walk and local snacks" },
                { place: "Tsomgo Lake", activity: "Scenic drive and lake photography" },
                { place: "Rumtek Monastery", activity: "Spiritual visit and peaceful environment" },
                { place: "Ban Jhakri Falls", activity: "Nature walk and waterfall time" },
                { place: "Nathula Pass", activity: "Mountain drive and high-altitude sightseeing" },
                { place: "Flower Exhibition Centre", activity: "Botanical stroll" }
            ],
            "leh": [
                { place: "Pangong Lake", activity: "Lake visit and sunrise experience" },
                { place: "Khardung La", activity: "High-altitude drive and viewpoint stop" },
                { place: "Shanti Stupa", activity: "Peaceful visit and sunset view" },
                { place: "Leh Palace", activity: "Heritage exploration" },
                { place: "Magnetic Hill", activity: "Phenomenon viewpoint and photo stop" },
                { place: "Thiksey Monastery", activity: "Monastery visit and spiritual calm" }
            ],
            "udaipur": [
                { place: "Lake Pichola", activity: "Boat ride and sunset cruise" },
                { place: "City Palace", activity: "Royal heritage walk" },
                { place: "Jag Mandir", activity: "Island visit and lakeside relaxation" },
                { place: "Saheliyon Ki Bari", activity: "Garden stroll and leisure time" },
                { place: "Bagore Ki Haveli", activity: "Cultural performance and local history" },
                { place: "Fateh Sagar Lake", activity: "Lakefront walk and café stop" }
            ],
            "jaisalmer": [
                { place: "Jaisalmer Fort", activity: "Heritage walk and fort exploration" },
                { place: "Patwon Ki Haveli", activity: "Historic architecture visit" },
                { place: "Sam Sand Dunes", activity: "Camel safari and desert evening" },
                { place: "Gadisar Lake", activity: "Peaceful lakeside stroll" },
                { place: "Bada Bagh", activity: "Sunset view and photography" },
                { place: "Desert camp", activity: "Cultural music and stargazing" }
            ],
            "kochi": [
                { place: "Fort Kochi", activity: "Heritage walk and sunset by the coast" },
                { place: "Chinese Fishing Nets", activity: "Photography and harbor walk" },
                { place: "Mattancherry Palace", activity: "Art and culture visit" },
                { place: "Jew Town", activity: "Shopping and cafés" },
                { place: "Marine Drive", activity: "Evening promenade and local snacks" },
                { place: "Cherai Beach", activity: "Beach relaxation and water fun" }
            ],
            "mysore": [
                { place: "Mysore Palace", activity: "Evening palace visit and illumination" },
                { place: "Chamundi Hills", activity: "Temple visit and panoramic drive" },
                { place: "Brindavan Gardens", activity: "Evening garden walk" },
                { place: "St. Philomena's Church", activity: "Church architecture visit" },
                { place: "Devaraja Market", activity: "Local shopping and food stroll" },
                { place: "Lalbagh Palace", activity: "Heritage sightseeing" }
            ]
        };

        if (itineraryIdeas[destinationKey]) {
            return itineraryIdeas[destinationKey].slice(0, 5);
        }

        const catalog =
            window.PLAN_MYYATRA_ITINERARY_CATALOG;
        const catalogKey =
            String(catalogDestination || destination || "")
                .trim()
                .toLowerCase();
        const destinationSpots =
            catalog?.destinations?.[catalogKey]?.spots ||
            catalog?.destinations?.[destinationKey]?.spots;

        if (!Array.isArray(destinationSpots)) {
            return [];
        }

        return destinationSpots.slice(0, 5);
    }

    function createItinerary(
        days,
        destination,
        selectedTheme = "balanced",
        catalogDestination = destination
    ) {

        const numberOfDays =
            Math.max(
                Number(days || 1),
                1
            );

        const destinationName =
            destination || "your destination";

        const itineraryIdeas =
            getDestinationItineraryIdeas(
                destinationName,
                catalogDestination
            );

        const uniqueIdeas =
            itineraryIdeas.filter(
                (item, index, array) =>
                    array.findIndex(
                        (candidate) => candidate.place === item.place
                    ) === index
            );

        if (uniqueIdeas.length === 0) {
            return `
                    <p class="itinerary-empty" role="status">
                        We don’t have verified place highlights for
                        ${escapeHTML(destinationName)} in the offline itinerary
                        catalog yet, so we haven’t filled this plan with guessed
                        attractions.
                    </p>
            `;
        }

        const theme =
            itineraryThemes[selectedTheme]
                    ? selectedTheme
                : "balanced";

        if (theme !== "balanced") {
            uniqueIdeas.sort((first, second) => {
                const firstMatches =
                    matchesItineraryTheme(first, theme);
                const secondMatches =
                    matchesItineraryTheme(second, theme);

                return Number(secondMatches) - Number(firstMatches);
            });
        }

        const totalSlots = uniqueIdeas.length;

        const baseCount =
            Math.floor(
                totalSlots / numberOfDays
            );

        const remainderCount =
            totalSlots % numberOfDays;

        const assignments = [];

        for (let day = 1; day <= numberOfDays; day++) {

            let count = baseCount;

            if (day <= remainderCount) {
                count += 1;
            }

            if (count === 0 && totalSlots > 0) {
                count = 1;
            }

            assignments.push(count);
        }

        const dayPlans = [];
        let cursor = 0;

        for (let day = 1; day <= numberOfDays; day++) {

            const count = assignments[day - 1] || 0;
            const items = uniqueIdeas.slice(cursor, cursor + count);

            dayPlans.push(items);
            cursor += count;
        }

        let html = "";

        for (
            let day = 1;
            day <= numberOfDays;
            day++
        ) {

            let title;

            if (day === 1) {
                title = "Arrival & Local Highlights";
            } else if (day === numberOfDays) {
                title = "Final Sightseeing & Departure";
            } else if (day === 2) {
                title = "Major Attractions Day";
            } else {
                title = `Explore ${destinationName}`;
            }

            const description =
                itineraryThemes[theme].description(destinationName);

            const items = dayPlans[day - 1] || [];

            const placeList =
                items.map(({ place, activity, osm }) => `
                    <li>
                        ${osm
                            ? `<a class="itinerary-place" href="${escapeHTML(osm)}" target="_blank" rel="noopener noreferrer">${escapeHTML(place)}</a>`
                            : `<span class="itinerary-place">${escapeHTML(place)}</span>`
                        }
                        <span class="itinerary-activity">${escapeHTML(activity)}</span>
                    </li>
                `).join("");

            if (items.length === 0) {
                title = "Flexible Day";
            }

            html += `
                <article class="itinerary-day itinerary-day-${theme}">

                    <div class="day-content">

                        <div class="itinerary-day-heading">
                            <span class="day-number">${String(day).padStart(2, "0")}</span>
                            <div>
                                <p class="itinerary-day-label">DAY ${day}</p>
                                <h4>${title}</h4>
                            </div>
                        </div>

                        <p class="itinerary-day-description">
                            ${escapeHTML(items.length
                                ? description
                                : `Keep this extra day flexible for rest, travel, or your own discoveries in ${destinationName}.`
                            )}
                        </p>

                        ${items.length
                            ? `<ul class="itinerary-places">${placeList}</ul>`
                            : ""
                        }

                    </div>

                </article>
            `;
        }

        if (uniqueIdeas.some((idea) => idea.source === "OpenStreetMap")) {
            html += `
                <p class="itinerary-attribution">
                    Mapped place highlights are sourced from
                    <a
                        href="https://www.openstreetmap.org/copyright"
                        target="_blank"
                        rel="noopener noreferrer"
                    >OpenStreetMap contributors</a>
                    (ODbL).
                </p>
            `;
        }

        return html;
    }


    // =========================================================
    // HOTEL TIER
    // =========================================================

    function getHotelTierFromBudget(
        budget,
        days,
        travelers,
        hotelPrices
    ) {

        const nights =
            Math.max(
                Number(days || 1) - 1,
                1
            );

        const rooms =
            Math.max(
                Math.ceil(
                    Number(travelers || 1) / 2
                ),
                1
            );

        const approximateHotelBudget =
            Number(budget || 0) * 0.25;

        const tiers = [
            "luxury",
            "premium",
            "standard",
            "budget"
        ];

        for (const tier of tiers) {

            const price =
                Number(
                    hotelPrices[tier] || 0
                );

            const total =
                price *
                nights *
                rooms;

            if (
                total <=
                approximateHotelBudget
            ) {
                return tier;
            }
        }

        return "budget";
    }


    // =========================================================
    // TRANSPORT NAME
    // =========================================================

    function getTransportName(mode) {

        const names = {
            road: "Road / Car",
            train: "Train",
            flight: "Flight",
            bus: "Bus",
            combination: "Combination"
        };

        return (
            names[mode] ||
            "Road / Car"
        );
    }


    // =========================================================
    // TRANSPORT ICON
    // =========================================================

    function getTransportIcon(mode) {

        const icons = {
            road: "🚗",
            train: "🚆",
            flight: "✈️",
            bus: "🚌",
            combination: "🔄"
        };

        return (
            icons[mode] ||
            "🚗"
        );
    }


    // =========================================================
    // NUMBER FORMAT
    // =========================================================

    function formatNumber(number) {

        const numericValue =
            Number(number || 0);

        return numericValue.toLocaleString(
            "en-IN",
            {
                maximumFractionDigits: 0
            }
        );
    }


    // =========================================================
    // CAPITALIZE
    // =========================================================

    function capitalize(value) {

        if (!value) {
            return "";
        }

        return String(value)
            .replace(/_/g, " ")
            .replace(/\b\w/g, char =>
                char.toUpperCase()
            );
    }


    // =========================================================
    // ESCAPE HTML
    // =========================================================

    function escapeHTML(value) {

        return String(value ?? "")
            .replace(
                /&/g,
                "&amp;"
            )
            .replace(
                /</g,
                "&lt;"
            )
            .replace(
                />/g,
                "&gt;"
            )
            .replace(
                /"/g,
                "&quot;"
            )
            .replace(
                /'/g,
                "&#039;"
            );
    }

});