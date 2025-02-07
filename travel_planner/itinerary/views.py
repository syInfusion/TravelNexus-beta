from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Itinerary
from users.models import Profile
from .utils.weather import get_weather
from .utils.recommendations import generate_itinerary, generate_recommendations

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


@login_required
def itinerary_view(request):
    """Generates or fetches the user’s personalized itinerary."""
    
    # Get user profile
    user_profile = Profile.objects.get(user=request.user)

    # Fetch or create itinerary
    itinerary, created = Itinerary.objects.get_or_create(user=request.user)

    # Fetch weather data
    weather_data = get_weather(itinerary.destination)

    # Generate AI-powered recommendations
    recommendations = generate_recommendations(user_profile, weather_data)

    # Update itinerary with recommendations and weather
    itinerary.weather_conditions = weather_data
    itinerary.recommendations = recommendations
    itinerary.save()

    return render(request, "itinerary/my_itinerary.html", {
        "itinerary": itinerary,
        "weather": weather_data,
        "recommendations": recommendations
    })