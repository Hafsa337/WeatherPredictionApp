from flask import Blueprint, jsonify, request, render_template
import requests

main = Blueprint('main', __name__)

API_KEY = "50f692a70ff64a4693663334261903"  # Replace with your WeatherAPI key

@main.route('/')
def home():
    return render_template("index.html")

@main.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.json.get('city', '').strip()
    if not city:
        return jsonify({"error": "City is required"})

    # WeatherAPI URL
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"

    try:
        response = requests.get(url)
        data = response.json()

        # Check for error
        if "error" in data:
            return jsonify({"error": data["error"]["message"]})

        current = data["current"]
        location = data["location"]

        weather = {
            "city": location["name"],
            "region": location["region"],
            "country": location["country"],
            "temperature": current["temp_c"],
            "condition": current["condition"]["text"],
            "humidity": current["humidity"],
            "wind": current["wind_kph"],
            "icon": current["condition"]["icon"]
        }

        return jsonify(weather)

    except Exception as e:
        print(e)
        return jsonify({"error": "Unable to fetch weather data"})