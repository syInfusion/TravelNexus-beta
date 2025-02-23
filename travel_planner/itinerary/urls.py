from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import home, profile
from .views import itinerary_view, ContactView,  AboutView,  ServicesView

urlpatterns = [
    path('home/', home, name='home'),
    path('profile/', profile, name='profile'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('my-itinerary/', itinerary_view, name='my-itinerary'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('services/', ServicesView.as_view(), name='services'),
    
]
