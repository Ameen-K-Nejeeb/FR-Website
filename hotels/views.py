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

    context = {
        "hotel": hotel,
    }

    return render(
        request,
        "hotels/hotel_detail.html",
        context
    )