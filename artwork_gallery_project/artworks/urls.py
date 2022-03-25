from django.contrib.auth.decorators import login_required
from django.urls import path
from artworks import views

urlpatterns = [
    path("", views.gallery, name="gallery"),
    path("<int:id>", views.artwork_detail, name="artwork_detail"),
]
