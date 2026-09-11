from django.shortcuts import render, redirect
from .models import Enquiry
from hotels.models import Hotel
from packages.models import Package


def enquiry_create(request):

    hotels = Hotel.objects.filter(available=True)
    packages = Package.objects.filter(available=True)

    if request.method == "POST":
        Enquiry.objects.create(
            customer_name=request.POST.get("customer_name"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
            hotel_id=request.POST.get("hotel") or None,
            package_id=request.POST.get("package") or None,
            travel_date=request.POST.get("travel_date") or None,
            adults=request.POST.get("adults") or 1,
            children=request.POST.get("children") or 0,
            message=request.POST.get("message"),
        )

        return redirect("enquiry_success")

    selected_hotel = request.GET.get("hotel")
    selected_package = request.GET.get("package")

    context = {
        "hotels": hotels,
        "packages": packages,
        "selected_hotel": selected_hotel,
        "selected_package": selected_package,
    }

    return render(request, "enquiries/enquiry_form.html", context)


def enquiry_success(request):
    return render(request, "enquiries/enquiry_success.html")