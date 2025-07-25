import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        return "API key not found."

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)

    if response.status_code != 200:
        return "Failed to fetch weather data."

    data = response.json()

    if "error" in data:
        return f"Error: {data['error']['message']}"

    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    return f"The current weather in {city} is {temp_c}°C with {condition}."

# Test cases
cities = ["Karachi", "Lahore", "New York", "Tokyo"]

for city in cities:
    print(get_weather(city))
