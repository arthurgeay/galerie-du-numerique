from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required


@login_required()
@permission_required("artworks.can_add")
def create_artwork(request):
    
    return render(request, "admin_interface/create_artwork.html")

@login_required()
@permission_required("artworks.can_change")
def edit_artwork(request, artwork_id):
    return render(request, "admin_interface/edit_artwork.html")

@login_required()
@permission_required("artworks.can_add")
def create_artist(request):
    return render(request, "admin_interface/create_artist.html")

@login_required()
@permission_required("artworks.can_view")
def view_artworks(request):
    return render(request, "admin_interface/view_artworks.html")