from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
# Create your models here.

class Profile(models.Model):
    """Defines user profile class"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=12, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    info = models.TextField(null=True, blank=True, max_length=100)
    bio = models.TextField(null=True, blank=True)  # Add bio field
    budget = models.CharField(max_length=50, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium')
    travel_preferences = models.JSONField(default=list)  # Stores as a list
    

    def __str__(self):
        return str(self.user)
    
    @property
    def name(self):
        if self.username:
            name = self.username
        else:
            name = self.user.username

        return name
    

    @property
    def avatar(self):
        """Defines a method to return the user's profile picture or a default avatar."""
        if self.profile_picture and hasattr(self.profile_picture, 'url'):
            return self.profile_picture.url  #  Return uploaded profile picture
        return static('images/avatar.svg')  #  Return default avatar if no picture