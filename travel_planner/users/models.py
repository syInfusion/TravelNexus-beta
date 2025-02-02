from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
# Create your models here.

class Profile(models.Model):
    """Defines user profile class"""
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    username =  models.CharField(max_length=12, null=True, blank=True)
    user_pic = models.ImageField(upload_to="avatars/", null=True, blank=True)
    info = models.TextField(null=True, blank=True, max_length=100)
    

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
        """Defines a  method to assign a default avatar to a user."""
        try:
            avatar = self.user_pic.url
        except:
            avatar =  static('images/avatar.svg')

        return avatar