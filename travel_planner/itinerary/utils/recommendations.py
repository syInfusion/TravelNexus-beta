from ..models import Itinerary
from users.models import Profile

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
