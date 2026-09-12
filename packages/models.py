from django.db import models
from django.utils.text import slugify

from hotels.models import Hotel


class Package(models.Model):
    name = models.CharField(max_length=200)

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    destination = models.CharField(
        max_length=200
    )

    description = models.TextField()

    duration_days = models.PositiveIntegerField()

    duration_nights = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    image = models.ImageField(
    upload_to="packages/",
    blank=True,
    null=True
)

    hotels = models.ManyToManyField(
        Hotel,
        blank=True,
        related_name="packages"
    )
    

    featured = models.BooleanField(
        default=False
    )

    available = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class PackageItinerary(models.Model):
    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE,
        related_name="itineraries"
    )
    day = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        ordering = ["day"]
        unique_together = ["package", "day"]

    def __str__(self):
        return f"{self.package.name} - Day {self.day}: {self.title}"

class PackageImage(models.Model):

    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(
        upload_to="packages/"
    )

    caption = models.CharField(
        max_length=200,
        blank=True
    )

    def __str__(self):
        return f"{self.package.name} - Image"