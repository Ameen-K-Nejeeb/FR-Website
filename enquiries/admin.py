from django.contrib import admin

from .models import Enquiry


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):

    list_display = (
        "customer_name",
        "phone",
        "package",
        "hotel",
        "travel_date",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "travel_date",
        "created_at",
    )

    search_fields = (
        "customer_name",
        "phone",
        "email",
    )

    list_editable = (
        "status",
    )