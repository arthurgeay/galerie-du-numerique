from django.urls import path
from artworks.views import ArtworkDetailView

urlpatterns = [
    path("artworks/<int:id>", ArtworkDetailView.as_view(), name="artwork_detail")
]
