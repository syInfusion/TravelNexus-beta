from ..models import Itinerary
from users.models import Profile
import random

def generate_itinerary(user):
    """Generate a personalized itinerary based on user profile and preferences."""
    profile = Profile.objects.get(user=user)
    
    # Dummy recommended destinations based on budget and preferences
    recommendations = {
        "low": ["Bangkok, Thailand", "Bali, Indonesia", "Kathmandu, Nepal"],
        "medium": ["Barcelona, Spain", "Cape Town, South Africa", "Lisbon, Portugal"],
        "high": ["Paris, France", "Maldives", "New York, USA"]
    }
    
    # Pick a destination based on budget
    recommended_destinations = recommendations.get(profile.budget, [])
    
    if recommended_destinations:
        suggested_destination = recommended_destinations[0]  # Just pick the first for now
    else:
        suggested_destination = "Unknown Destination"

    # Example of activities
    activity_options = {
        "beach": ["Snorkeling", "Boat Ride", "Sunbathing"],
        "adventure": ["Hiking", "Skydiving", "Zip-lining"],
        "culture": ["Museum Visit", "Local Market Tour", "Historical Sites"]
    }
    
    selected_activities = []
    for pref in profile.travel_preferences:
        selected_activities.extend(activity_options.get(pref, []))

    # Create a new itinerary entry
    itinerary = Itinerary.objects.create(
        user=user,
        destination=suggested_destination,
        start_date="2025-03-10",  # Dummy date for now
        end_date="2025-03-15",
        activities=selected_activities,
        budget=profile.budget,
        preferences=profile.travel_preferences
    )

    return itinerary

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