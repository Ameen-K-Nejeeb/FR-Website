from django.shortcuts import render

from hotels.models import Hotel
from packages.models import Package


def home(request):
    featured_hotels = Hotel.objects.filter(
        featured=True,
        available=True
    )[:6]

    featured_packages = Package.objects.filter(
        featured=True,
        available=True
    )[:6]

    context = {
        "featured_hotels": featured_hotels,
        "featured_packages": featured_packages,
    }

    return render(request, "home.html", context)