from django.contrib import admin

from .models import Package


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "destination",
        "duration_days",
        "duration_nights",
        "price",
        "featured",
        "available",
    )

    list_filter = (
        "featured",
        "available",
        "destination",
    )

    search_fields = (
        "name",
        "destination",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }