from django.urls import path
from artworks.views import ArtworkDetailView
from artworks import views

urlpatterns = [
    path("", views.gallery, name="galery"),
    path("<int:id>", ArtworkDetailView.as_view(), name="artwork_detail"),
]
