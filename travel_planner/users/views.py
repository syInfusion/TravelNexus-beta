from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile
from .serializer import ProfileSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

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
        # Save profile details from form submission
        profile.bio = request.POST.get('bio', '')
        profile.budget = request.POST.get('budget', 'medium')
        profile.travel_preferences = request.POST.get('travel_preferences', '')
        profile.save()
        
        # Redirect to personalized home page after completion
        return redirect('home')

    return render(request, 'users/profile_setup.html', {'profile': profile})