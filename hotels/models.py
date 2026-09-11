from django.db import models
from django.utils.text import slugify


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)

    location = models.CharField(max_length=200)

    description = models.TextField()

    price_per_night = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=0
    )

    amenities = models.TextField(
        blank=True,
        help_text="Example: WiFi, Pool, Parking, Breakfast"
    )

    featured = models.BooleanField(default=False)
    available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class HotelImage(models.Model):
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(upload_to="hotels/")

    caption = models.CharField(
        max_length=200,
        blank=True
    )

    def __str__(self):
        return f"{self.hotel.name} - Image"