from django.urls import path
from .views import enquiry_create, enquiry_success


urlpatterns = [
    path("", enquiry_create, name="enquiry_create"),
    path("success/", enquiry_success, name="enquiry_success"),
]