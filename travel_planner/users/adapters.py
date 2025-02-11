from allauth.account.adapter import DefaultAccountAdapter
from django.shortcuts import resolve_url

class MyAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        print("🔹 Custom Adapter is Running...")  # Debugging line

        user = request.user

        # Check if the user has a profile and if their bio is empty
        if not hasattr(user, 'profile') or not user.profile.bio:
            print("🔸 Redirecting user to profile setup...")  # Debugging line
            return resolve_url('profile-setup')

        print("✅ Profile is complete, redirecting to home...")  # Debugging line
        return resolve_url('home')
