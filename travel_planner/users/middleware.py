from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    """
    Redirects users to profile setup if their profile is incomplete.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.path not in [reverse('profile-setup'), reverse('logout')]:  # Allow profile setup & logout pages
                if not hasattr(request.user, 'profile') or not request.user.profile.bio:
                    return redirect('profile-setup')
        return self.get_response(request)
