from django.shortcuts import render


# Create your views here.
#view to the basic home page

def home(request):
    """Returns the base template."""

    return render(request, 'home/home.html')