from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import home, profile
from .views import itinerary_view,  edit_itinerary_view
from . import views

urlpatterns = [
    path('home/', home, name='home'),
    path('profile/', profile, name='profile'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('my-itinerary/', itinerary_view, name='my-itinerary'),
    path("edit-itinerary/", edit_itinerary_view, name="edit_itinerary"),
    path('itinerary/my-itinerary/', views.itinerary_view, name='itinerary_view'),
]
