from django.urls import path
from .views import ProfileDetailView, profile_setup, landing_page
from django.contrib.auth.views import LogoutView

urlpatterns =  [
    path('profile-setup/', profile_setup, name='profile-setup'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/', ProfileDetailView.as_view(), name='profile-detail'),
    path('', landing_page, name='landing-page')
]