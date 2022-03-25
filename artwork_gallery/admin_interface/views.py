from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from admin_interface.forms import CreateForm, UpdateForm, CreateArtistForm


@login_required()
@permission_required("artworks.can_add")
def create_artwork(request):
    form = CreateForm()
    return render(request,  "admin_interface/create_artwork.html", {'form': form})

@login_required()
@permission_required("artworks.can_change")
def edit_artwork(request, artwork_id):
    form = UpdateForm()
    return render(request,  "admin_interface/edit_artwork.html", {'form': form})

@login_required()
@permission_required("artworks.can_add")
def create_artist(request):
    form = CreateArtistForm()
    return render(request, "admin_interface/create_artist.html", {'form': form})

@login_required()
@permission_required("artworks.can_view")
def view_artworks(request):
    return render(request, "admin_interface/view_artworks.html")