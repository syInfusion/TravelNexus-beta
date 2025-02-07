from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Itinerary(models.Model):
    """Stores personalized itinerary details for each user"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.CharField(max_length=255)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True)
    budget = models.CharField(
        max_length=50, 
        choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], 
        default='medium'
    )
    activities = models.JSONField(default=list)  # Stores a list of activities
    weather_conditions = models.JSONField(default=dict)  # Stores weather data
    recommendations = models.JSONField(default=dict)  # Stores AI-generated recommendations

    def __str__(self):
        return f"Itinerary for {self.user.username} - {self.destination}"
