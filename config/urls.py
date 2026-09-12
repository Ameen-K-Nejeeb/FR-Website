from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .views import home

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home, name="home"),

    path("hotels/", include("hotels.urls")),
    path("packages/", include("packages.urls")),
    path("enquiries/", include("enquiries.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )