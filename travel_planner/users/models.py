from django.db import models

# Create your models here.
from django.contrib.auth.models import  User
from django.templatetags import static


class Profile(models.Model):
    """Define the user profile model."""
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    displayname =  models.CharField(max_length=20, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='avatars/', null=True, blank=True)
    info = models.TextField(blank=True, null=True)


    def __str__(self):
        return str(self.user)
    

    @property
    def name(self):
        """If user does not provide displayname."""
        if self.displayname:
            name = self.displayname
        else:
            name =  self.user.username

        return name
    

    @property
    def profile(self):
        """Sets user profile to the default if the user profile has not been provided."""
        try:
            profile = self.profile_pic.url
        except:
            profile = static('static/avatar.svg')

        return profile