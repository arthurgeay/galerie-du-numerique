from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from admin_interface.forms import CreateForm, UpdateForm, CreateArtistForm
from django.core.paginator import Paginator
from artworks.models import Artwork, Artist


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
    artwork_list = Artwork.objects.all()

    paginator = Paginator(artwork_list, 4)
    page = request.GET.get("page")
    artworks = paginator.get_page(page)

    return render(request, "admin_interface/view_artworks.html", {"artworks": artworks})