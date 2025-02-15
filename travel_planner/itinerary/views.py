from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Itinerary
from django.contrib import messages
from django.utils.dateparse import parse_date
import datetime
from users.models import Profile
from .utils.weather import get_weather_data
from .utils.recommendations import generate_recommendations

@login_required
def home(request):
    destinations = [
        {"name": "Santorini", "image_url": "/static/images/santorini.jpg", "description": "Beautiful island in Greece.", "price": 1500},
        {"name": "Bali", "image_url": "/static/images/bali.jpg", "description": "Exotic paradise with stunning beaches.", "price": 1200},
        {"name": "Paris", "image_url": "/static/images/paris.jpg", "description": "Romantic city with iconic landmarks.", "price": 1800},
    ]
    return render(request, 'home/home.html', {'user': request.user, 'destinations': destinations})


def profile(request):
    return render(request, 'home/profile.html')

# Activity-to-City mapping
ACTIVITY_TO_CITY = {
    "adventure": "Queenstown",
    "beach": "Maldives",
    "culture": "Kyoto",
    "nightlife": "Las Vegas",
    "history": "Rome",
    "nature": "Cape Town",
    "food": "Bangkok",
    "safari": "Nairobi"
}

def itinerary_view(request):
    """Handles itinerary generation and displays it to the user."""
    user = request.user

    # Debug: Check stored travel preferences
    travel_prefs = user.profile.travel_preferences
    print("User Travel Preferences:", travel_prefs)

    # Extract first activity and map it to a city
    activity = travel_prefs[0] if travel_prefs else None
    city = ACTIVITY_TO_CITY.get(activity, "Nairobi")  # Default to Nairobi

    print("Mapped City:", city)

    # Fetch weather data
    weather_data = get_weather_data(city)
    print("Weather Data:", weather_data)

    # Ensure weather_data is never None
    if not weather_data or "error" in weather_data:
        weather_data = {"temperature": "N/A", "condition": "N/A"}

    # Generate recommendations for activities in the city
    recommended_activities = generate_recommendations(user.profile, weather_data)
    print("Recommended Activities:", recommended_activities)

    # Create or update the user's itinerary
    itinerary, created = Itinerary.objects.get_or_create(
        user=user,
        defaults={"destination": city, "weather_conditions": weather_data}
    )

    # Ensure destination updates correctly
    if not created:
        itinerary.destination = city
        itinerary.weather_conditions = weather_data
        itinerary.save()

    return render(request, "itinerary/my_itinerary.html", {
        "itinerary": itinerary,
        "recommended_activities": recommended_activities
    })
    
@login_required
def edit_itinerary_view(request):
    """Allow users to edit their itinerary"""
    user = request.user
    itinerary = Itinerary.objects.get(user=user)

    if request.method == "POST":
        destination = request.POST.get("destination")
        start_date = parse_date(request.POST.get("start_date"))
        end_date = parse_date(request.POST.get("end_date"))
        budget = request.POST.get("budget")
        activities = request.POST.getlist("activities")  # Get multiple activities
        
        # 🛑 **Validation: Prevent end date before start date**
        if end_date and start_date and end_date < start_date:
            messages.error(request, "End date cannot be before the start date.")
            return redirect("edit_itinerary")

        # ✅ **Update the itinerary**
        itinerary.destination = destination
        itinerary.start_date = start_date
        itinerary.end_date = end_date
        itinerary.budget = budget
        itinerary.activities = activities  # Ensure activities are updated
        itinerary.save()

        return redirect("itinerary_view")  # Redirect to itinerary page

    return render(request, "itinerary/edit_itinerary.html", {"itinerary": itinerary})   