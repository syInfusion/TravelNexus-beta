from django.urls import path
from .views import ProfileDetailView
from django.contrib.auth.views import LogoutView

urlpatterns =  [
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/', ProfileDetailView.as_view(), name='profile-detail')
]