from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Itinerary
from users.models import Profile
from .utils.weather import get_weather_data
from .utils.recommendations import generate_recommendations
from django.views.generic import View

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
        weather_data = {"temperature": "N/A", "condition": "N/A"}  # Fixed key

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
    


class AboutView(View):
    """Defines the about page view to display info about Travel Planner."""
    template =  'home/about.html'

    def get(self, request):
        return render(request, self.template)


class ContactView(View):
    """Defines the contact page view to display contact info for Travel Planner."""
    template = 'home/contacts.html'
    
    def get(self, request):
        return render(request, self.template)
    

class ServicesView(View):
    """Defines the services page view to display services offered by Travel Planner."""
    template = 'home/services.html'
    
    def get(self, request):
        return render(request, self.template)
    