from django.contrib import admin

from .models import Hotel, HotelImage


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "price_per_night",
        "rating",
        "featured",
        "available",
    )

    list_filter = (
        "featured",
        "available",
        "location",
    )

    search_fields = (
        "name",
        "location",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }


@admin.register(HotelImage)
class HotelImageAdmin(admin.ModelAdmin):
    list_display = (
        "hotel",
        "caption",
    )