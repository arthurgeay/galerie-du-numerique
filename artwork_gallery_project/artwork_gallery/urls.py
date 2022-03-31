from django.urls import path, include
from django.conf.urls import handler404, handler500, handler403


urlpatterns = [
    path("", include("authentication.urls")),
    path("", include("presentation.urls")),
    path("artworks/", include("artworks.urls")),
    path("polls/", include("polls.urls")),
    path("admin/", include("admin_interface.urls"), name="admin"),
]

handler403 = "artworks.views.error_403"
handler404 = "artworks.views.error_404"
handler500 = "artworks.views.error_500"
