from django.urls import path

from .views import hotel_detail, hotel_list


urlpatterns = [
    path(
        "",
        hotel_list,
        name="hotel_list"
    ),

    path(
        "<slug:slug>/",
        hotel_detail,
        name="hotel_detail"
    ),
]