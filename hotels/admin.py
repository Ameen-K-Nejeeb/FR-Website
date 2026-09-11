from django.contrib import admin
from .models import Hotel, HotelImage


class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 3


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "price_per_night",
        "rating",
        "available",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    inlines = [HotelImageInline]


@admin.register(HotelImage)
class HotelImageAdmin(admin.ModelAdmin):
    list_display = (
        "hotel",
        "caption",
    )