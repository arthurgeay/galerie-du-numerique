from django.contrib.auth.decorators import login_required
from django.urls import path
from artworks import views
from artworks.views import ArtworkDetailView

urlpatterns = [
    path("", views.gallery, name="galery"),
    path(
        "<int:id>", login_required(ArtworkDetailView.as_view()), name="artwork_detail"
    ),
]
