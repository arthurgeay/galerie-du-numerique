from django.urls import path
from admin_interface import views

urlpatterns = [
    # Artworks
    path("", views.view_artworks, name="view_artworks"),
    path("artworks/create/", views.create_artwork, name="create_artwork"),
    path("artworks/edit/<int:artwork_id>/", views.edit_artwork, name="edit_artwork"),
    path(
        "artworks/delete/<int:artwork_id>", views.delete_artwork, name="delete_artwork"
    ),
    # Artists
    path("artists", views.view_artists, name="view_artists"),
    path("artists/create/", views.create_artist, name="create_artist"),
    path("artists/edit/<int:artist_id>/", views.edit_artist, name="edit_artist"),
    path("artists/delete/<int:artist_id>", views.delete_artist, name="delete_artist"),
]
