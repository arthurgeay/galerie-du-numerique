from django.urls import path
from admin_interface import views

urlpatterns = [
    path("", views.view_artworks, name="view_artworks"),
    path("create/", views.create_artwork, name="create_artwork"),
    path("edit/<int:artwork_id>/", views.edit_artwork, name="edit_artwork"),
    path("create-artist/", views.create_artist, name="create_artist"),
    path(
        "delete-artwork/<int:artwork_id>", views.delete_artwork, name="delete_artwork"
    ),
]
