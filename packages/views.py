from django.shortcuts import get_object_or_404, render
from .models import Package


def package_list(request):
    packages = Package.objects.filter(available=True)

    context = {
        "packages": packages,
        "featured_packages": packages,  # matches {% for package in featured_packages %}
    }

    return render(request, "packages/package_list.html", context)


def package_detail(request, slug):
    package = get_object_or_404(
        Package.objects.prefetch_related("images", "itineraries", "hotels"),
        slug=slug,
        available=True,
    )

    context = {
        "package": package,
    }

    return render(request, "packages/package_detail.html", context)


def about(request):
    return render(request, "about.html")


