from django.contrib import admin
from .models import Package, PackageImage


class PackageImageInline(admin.TabularInline):
    model = PackageImage
    extra = 3


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "destination",
        "price",
        "duration_days",
        "duration_nights",
        "featured",
        "available",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    filter_horizontal = (
        "hotels",
    )

    inlines = [
        PackageImageInline
    ]


@admin.register(PackageImage)
class PackageImageAdmin(admin.ModelAdmin):

    list_display = (
        "package",
        "caption",
    )