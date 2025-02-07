from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile
from .serializer import ProfileSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect



def landing_page(request):
    """Landing page for unauthenticated users. Redirects authenticated users to home."""
    if request.user.is_authenticated:
        return redirect('home')  # Redirects authenticated users to their dashboard
    return render(request, 'home.html')  # Unauthenticated users see the landing page

class ProfileDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

@login_required
def profile_setup(request):
    """
    View to handle profile setup for new users.
    """
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        profile.bio = request.POST.get('bio', '')
        profile.budget = request.POST.get('budget', 'medium')
        profile.travel_preferences = request.POST.getlist('travel_preferences', '')

        # ✅ Properly handle profile picture uploads
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']

        profile.save()
        
        return redirect('home')  # Redirect after saving

    return render(request, 'users/profile_setup.html', {'profile': profile})