from django.urls import path
from artworks import views

urlpatterns = [
    path("", views.gallery, name="galery"),
]
