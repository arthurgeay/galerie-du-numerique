from django.contrib.auth.decorators import login_required
from django.urls import path
from admin import views

urlpatterns = [
    path("", views.view_artworks, name="view_artworks"),
    path("create/", views.create_artwork, name="create_artwork"),
    path("edit/<int:artwork_id>/", views.edit_artwork, name="edit_artwork"),
    path("create_artist/", views.create_artist, name="create_artist"),
]
