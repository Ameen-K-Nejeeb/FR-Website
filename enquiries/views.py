from django.shortcuts import render, redirect, get_object_or_404
from .models import Enquiry
from hotels.models import Hotel
from packages.models import Package


def enquiry_create(request):
    hotel_slug = request.GET.get("hotel")
    package_slug = request.GET.get("package")

    locked_hotel = get_object_or_404(Hotel, slug=hotel_slug) if hotel_slug else None
    
    # Prefetch the package's related hotels
    locked_package = (
        get_object_or_404(Package.objects.prefetch_related("hotels"), slug=package_slug)
        if package_slug
        else None
    )

    if request.method == "POST":
        hotel_id = locked_hotel.id if locked_hotel else (request.POST.get("hotel") or None)
        package_id = locked_package.id if locked_package else (request.POST.get("package") or None)

        Enquiry.objects.create(
            customer_name=request.POST.get("customer_name"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
            hotel_id=hotel_id,
            package_id=package_id,
            travel_date=request.POST.get("travel_date") or None,
            adults=request.POST.get("adults") or 1,
            children=request.POST.get("children") or 0,
            message=request.POST.get("message"),
        )
        return redirect("enquiry_success")

    hotels = Hotel.objects.filter(available=True) if not locked_hotel and not locked_package else []
    packages = Package.objects.filter(available=True) if not locked_hotel and not locked_package else []

    context = {
        "locked_hotel": locked_hotel,
        "locked_package": locked_package,
        "hotels": hotels,
        "packages": packages,
    }

    return render(request, "enquiries/enquiry_form.html", context)


def enquiry_success(request):
    return render(request, "enquiries/enquiry_success.html")