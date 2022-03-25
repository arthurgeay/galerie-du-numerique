from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # TODO: Deactivate admin django
    path("admin-django/", admin.site.urls),
    path("", include("authentication.urls")),
    path("", include("presentation.urls")),
    path("artworks/", include("artworks.urls")),
    path("polls/", include("polls.urls")),
    path("admin/", include("admin_interface.urls")),
]
