from django.shortcuts import get_object_or_404, render

from .models import Hotel


def hotel_list(request):
    hotels = Hotel.objects.filter(
        available=True
    )

    context = {
        "hotels": hotels,
    }

    return render(
        request,
        "hotels/hotel_list.html",
        context
    )


def hotel_detail(request, slug):
    hotel = get_object_or_404(
        Hotel,
        slug=slug,
        available=True
    )

    amenities = [
        amenity.strip()
        for amenity in hotel.amenities.split(",")
        if amenity.strip()
    ]


    context = {
        "hotel": hotel,
        "amenities": amenities
    }

    return render(
        request,
        "hotels/hotel_detail.html",
        context
    )


