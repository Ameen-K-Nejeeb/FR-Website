from django.db import models

from hotels.models import Hotel
from packages.models import Package


class Enquiry(models.Model):

    STATUS_CHOICES = [
        ("new", "New"),
        ("contacted", "Contacted"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    ]

    customer_name = models.CharField(
        max_length=200
    )

    phone = models.CharField(
        max_length=20
    )

    email = models.EmailField(
        blank=True
    )

    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="enquiries"
    )

    package = models.ForeignKey(
        Package,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="enquiries"
    )

    travel_date = models.DateField(
        null=True,
        blank=True
    )

    adults = models.PositiveIntegerField(
        default=1
    )

    children = models.PositiveIntegerField(
        default=0
    )

    message = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.customer_name} - {self.phone}"