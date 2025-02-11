import requests
from django.conf import settings
import os
import logging

logger = logging.getLogger(__name__)

API_KEY = os.getenv("API_KEY")  # Load API key from .env
BASE_URL = os.getenv("BASE_URL")  # Load API URL from .env


def get_weather_data(city):
    """Fetches weather data from OpenWeatherMap API."""
    
    if not city:  # Ensure city is not empty
        logger.error("City name is missing for weather API request")
        return {"error": "City name is required"}

    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP errors

        data = response.json()

        if "weather" in data and "main" in data:
            return {
                "condition": data["weather"][0]["main"],  # e.g., "Cloudy"
                "temperature": data["main"]["temp"]  # e.g., 23.5°C
            }
        else:
            logger.error(f"Invalid API response: {data}")
            return {"error": "Invalid API response"}

    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching weather data: {e}")
        return {"error": str(e)}