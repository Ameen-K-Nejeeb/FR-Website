from django.urls import path
from .views import package_list, package_detail, about


urlpatterns = [
    path("", package_list, name="package_list"),

    path("about/", about, name="about"),

    path("<slug:slug>/", package_detail, name="package_detail"),
]