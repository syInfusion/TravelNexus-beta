from ..models import Itinerary
from users.models import Profile
import random


def generate_recommendations(user_profile, weather_data):
    """Generates personalized activity recommendations based on user profile and weather."""
    
    activity_options = {
        "beach": ["Sunbathing", "Snorkeling", "Beach Volleyball"],
        "adventure": ["Hiking", "Bungee Jumping", "Skydiving"],
        "food": ["Street Food Tour", "Fine Dining Experience", "Cooking Class"],
        "city": ["Museum Tour", "Shopping", "Nightlife"]
    }
    
    # Determine recommended category based on weather
    if weather_data and weather_data["temperature"] > 25:
        preferred_activities = activity_options["beach"] + activity_options["food"]
    elif weather_data and "rain" in weather_data["weather"].lower():
        preferred_activities = activity_options["city"]
    else:
        preferred_activities = activity_options["adventure"] + activity_options["city"]

    # Personalize further based on user preferences
    user_prefs = user_profile.travel_preferences  # e.g., ["adventure", "food"]
    recommended = []

    for pref in user_prefs:
        if pref in activity_options:
            recommended.extend(activity_options[pref])

    # Shuffle and return top 3 recommendations
    random.shuffle(recommended)
    return recommended[:3] if recommended else preferred_activities[:3]