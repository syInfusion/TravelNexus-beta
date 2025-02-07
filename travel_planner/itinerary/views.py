from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Itinerary
from .utils.recommendations import generate_itinerary
from datetime import date, timedelta
from django.utils import timezone 

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
    """Ensure a user has only one itinerary and fetch it."""
    itinerary, created = Itinerary.objects.get_or_create(user=request.user, defaults={
        "start_date": timezone.now().date(),  # Set a default start date
        "end_date": timezone.now().date(),
    })

    # If multiple itineraries exist, get the most recent one
    if not created:
        itinerary = Itinerary.objects.filter(user=request.user).latest("created_at")

    return render(request, "itinerary/itinerary.html", {"itinerary": itinerary})