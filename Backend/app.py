from flask import Flask, request, jsonify
from flask_cors import CORS

try:
    from .travel_engine import (
        get_distance,
        get_destination_info,
        get_transport_hubs,
        recommend_transport,
        calculate_all_transport,
    )
except ImportError:
    from travel_engine import (
        get_distance,
        get_destination_info,
        get_transport_hubs,
        recommend_transport,
        calculate_all_transport,
    )


app = Flask(__name__)

# Allow the frontend to communicate with Flask
CORS(app)


# ==========================================
# HOME
# ==========================================

@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "success": True,
        "message": "Plan MyYatra backend is running!"
    })


# ==========================================
# PLAN TRIP
# ==========================================

@app.route("/api/plan-trip", methods=["POST"])
def plan_trip():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "success": False,
                "error": "No trip data was received."
            }), 400


        # ==========================================
        # GET USER INPUT
        # ==========================================

        from_location = str(
            data.get("from", "")
        ).strip()

        destination = str(
            data.get("destination", "")
        ).strip()

        days = int(
            data.get("days", 0)
        )

        travelers = int(
            data.get("travelers", 0)
        )

        budget = float(
            data.get("budget", 0)
        )

        transport_mode = str(
            data.get(
                "transport_mode",
                "auto"
            )
        ).lower()

        hotel_preference = str(
            data.get(
                "hotel_preference",
                "auto"
            )
        ).lower()


        # ==========================================
        # VALIDATION
        # ==========================================

        if not from_location:

            return jsonify({
                "success": False,
                "error": "Starting location is required."
            }), 400


        if not destination:

            return jsonify({
                "success": False,
                "error": "Destination is required."
            }), 400


        if days < 1:

            return jsonify({
                "success": False,
                "error": "Number of days must be at least 1."
            }), 400


        if travelers < 1:

            return jsonify({
                "success": False,
                "error": "Number of travelers must be at least 1."
            }), 400


        if budget <= 0:

            return jsonify({
                "success": False,
                "error": "Budget must be greater than 0."
            }), 400


        # ==========================================
        # DESTINATION INFORMATION
        # ==========================================

        destination_info = get_destination_info(
            destination
        )

        transport_hubs = get_transport_hubs(
            destination
        )


        # ==========================================
        # DISTANCE
        # ==========================================

        distance = get_distance(
            from_location,
            destination
        )


        if distance is None:

            return jsonify({
                "success": False,
                "error": (
                    "We currently do not have enough "
                    "route information for this city. "
                    "Please try another Indian city."
                )
            }), 400


        # ==========================================
        # TRANSPORT OPTIONS
        # ==========================================

        transport_options = calculate_all_transport(
            from_location,
            destination,
            travelers
        )


        # ==========================================
        # TRANSPORT RECOMMENDATION
        # ==========================================

        recommendation = recommend_transport(
            from_location,
            destination,
            travelers,
            budget,
            transport_mode
        )


        # ==========================================
        # RESULT
        # ==========================================

        result = {

            "success": True,

            "trip": {

                "from": from_location,

                "destination": destination,

                "days": days,

                "travelers": travelers,

                "budget": budget,

                "transport_mode": transport_mode,

                "hotel_preference": hotel_preference
            },


            "route": {

                "one_way_distance_km": distance,

                "round_trip_distance_km": round(
                    distance * 2,
                    1
                )
            },


            "destination_info": destination_info,


            "transport_hubs": transport_hubs,


            "transport": {

                "recommended": recommendation,

                "options": transport_options
            },


            "message": (
                "Your trip details and transport "
                "estimate were generated successfully."
            )
        }


        return jsonify(result), 200


    except ValueError:

        return jsonify({
            "success": False,
            "error": (
                "Please enter valid numbers for "
                "days, travelers and budget."
            )
        }), 400


    except Exception as error:

        print(
            "Backend Error:",
            error
        )

        return jsonify({
            "success": False,
            "error": (
                "An unexpected server error occurred."
            )
        }), 500


# ==========================================
# RUN SERVER
# ==========================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
