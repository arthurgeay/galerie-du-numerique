from django.urls import path, include
#from django.contrib import admin

urlpatterns = [
    #path("admin-django/", admin.site.urls),
    path("", include("authentication.urls")),
    path("", include("presentation.urls")),
    path("artworks/", include("artworks.urls")),
    path("polls/", include("polls.urls")),
    path("admin/", include("admin_interface.urls"), name="admin"),
]
