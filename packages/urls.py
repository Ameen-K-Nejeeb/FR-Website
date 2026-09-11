from django.urls import path
from .views import package_list, package_detail


urlpatterns = [
    path("", package_list, name="package_list"),
    path("<slug:slug>/", package_detail, name="package_detail"),
]