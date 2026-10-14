document.addEventListener("DOMContentLoaded", () => {
    const welcomeScreen = document.getElementById("welcomeScreen");
    const mainWebsite = document.getElementById("mainWebsite");
    const startPlanningBtn = document.getElementById("startPlanningBtn");

    if (window.gsap && window.ScrollTrigger) {
        gsap.registerPlugin(ScrollTrigger);
    }

    if (!welcomeScreen || !mainWebsite || !startPlanningBtn) {
        console.error("Required website elements were not found.");
        return;
    }

    if (window.gsap) {
        gsap.from(".welcome-content", {
            duration: 1.1,
            y: 40,
            opacity: 0,
            ease: "power3.out"
        });

        gsap.from(".hero-copy, .hero-panel", {
            duration: 1,
            y: 30,
            opacity: 0,
            stagger: 0.12,
            ease: "power3.out",
            delay: 0.2
        });

        gsap.from(".feature-card, .process-card, .about-content, .planner-card", {
            scrollTrigger: {
                trigger: ".feature-section, .process-section, .planner-section, .about-section",
                start: "top 80%"
            },
            duration: 0.85,
            y: 35,
            opacity: 0,
            stagger: 0.12,
            ease: "power3.out"
        });

        const revealItems = document.querySelectorAll(".reveal");

        revealItems.forEach((item) => {
            item.classList.remove("reveal");
        });
    }

    startPlanningBtn.addEventListener("click", () => {
        welcomeScreen.classList.add("hidden");
        mainWebsite.classList.remove("hidden");

        if (window.gsap) {
            gsap.from(".hero-copy, .hero-panel, .feature-card, .process-card", {
                duration: 0.8,
                y: 30,
                opacity: 0,
                stagger: 0.08,
                ease: "power3.out"
            });
        }

        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    });
});

function scrollToPlanner() {
    const plannerSection = document.getElementById("planner");

    if (plannerSection) {
        plannerSection.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    }
}