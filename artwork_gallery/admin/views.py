from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import path
from admin import views


@login_required()
@permission_required("artworks.can_add")
def create_artwork(request):
    return render(request, "artworks/create_artwork.html")

@login_required()
@permission_required("artworks.can_change")
def edit_artwork(request, artwork_id):
    return render(request, "artworks/edit_artwork.html")

@login_required()
@permission_required("artworks.can_add")
def create_artist(request):
    return render(request, "artworks/create_artist.html")

@login_required()
@permission_required("artworks.can_view")
def view_artworks(request):
    return render(request, "artworks/view_artworks.html")