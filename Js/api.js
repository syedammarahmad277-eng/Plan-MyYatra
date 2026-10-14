// ==========================================
// Plan MyYatra - API Connection
// ==========================================

// Local Flask backend
const API_URL = "http://127.0.0.1:5000/api/plan-trip";


// Send trip details to the Flask backend
async function planTrip(tripData) {
    try {
        const response = await fetch(API_URL, {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(tripData)
        });

        // Check whether the server returned an error
        if (!response.ok) {
            let errorMessage = "Something went wrong with the server.";

            try {
                const errorData = await response.json();

                if (errorData.error) {
                    errorMessage = errorData.error;
                }
            } catch (error) {
                // Response was not JSON
            }

            throw new Error(errorMessage);
        }

        // Convert server response into JavaScript object
        const data = await response.json();

        return data;

    } catch (error) {
        console.error("API Error:", error);

        throw error;
    }
}