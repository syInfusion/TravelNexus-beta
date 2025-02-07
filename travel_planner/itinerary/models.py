from django.db import models
from django.contrib.auth.models import User

class Itinerary(models.Model):
    """Stores a user's personalized travel plan."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.CharField(max_length=255)  # e.g., "Paris, France"
    start_date = models.DateField()
    end_date = models.DateField()
    activities = models.JSONField(default=list)  # List of planned activities
    budget = models.CharField(max_length=50, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    preferences = models.JSONField(default=list)  # Stores selected user preferences
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.destination}"
