from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    destinations = [
        {"name": "Santorini", "image_url": "/static/images/santorini.jpg", "description": "Beautiful island in Greece.", "price": 1500},
        {"name": "Bali", "image_url": "/static/images/bali.jpg", "description": "Exotic paradise with stunning beaches.", "price": 1200},
        {"name": "Paris", "image_url": "/static/images/paris.jpg", "description": "Romantic city with iconic landmarks.", "price": 1800},
    ]
    return render(request, 'home/home.html', {'user': request.user, 'destinations': destinations})


def profile(request):
    return render(request, 'itinerary/profile.html')
