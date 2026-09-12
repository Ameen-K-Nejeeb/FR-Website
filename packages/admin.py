from django.contrib import admin
from .models import Package, PackageImage, PackageItinerary


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = (
        "name",
        "destination",
        "price",
        "duration_days",
        "duration_nights",
        "featured",
        "available",
    )
    list_filter = ("featured", "available")
    search_fields = ("name", "destination")


@admin.register(PackageImage)
class PackageImageAdmin(admin.ModelAdmin):
    list_display = ("package", "caption")
    list_filter = ("package",)


@admin.register(PackageItinerary)
class PackageItineraryAdmin(admin.ModelAdmin):
    list_display = ("package", "day", "title")
    list_filter = ("package",)
    search_fields = ("package__name", "title", "description")
    ordering = ("package", "day")