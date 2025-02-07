import requests
from django.conf import settings
import os

API_KEY = os.getenv("API_KEY")  # Load API key from .env
BASE_URL = os.getenv("BASE_URL")  # Load API URL from .env

def get_weather(city):
    """Fetches real-time weather data for a given city"""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"]
        }
    
    return None  # Return None if API request fails
