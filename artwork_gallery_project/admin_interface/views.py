from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from admin_interface.forms import CreateForm, UpdateForm, ArtistForm
from django.core.paginator import Paginator
from artworks.models import Artwork, Artist
from django.contrib import messages

@login_required()
@permission_required("artworks.can_view")
def view_artworks(request):
    artwork_list = Artwork.objects.all().order_by("-id")

    paginator = Paginator(artwork_list, 4)
    page = request.GET.get("page")
    artworks = paginator.get_page(page)

    return render(request, "admin_interface/view_artworks.html", {"artworks": artworks})

@login_required()
@permission_required("artworks.can_add")
def create_artwork(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "{} a bien été sauvegardé.".format(form.cleaned_data["title"])
            )
            return redirect("view_artworks")
    else:
        form = CreateForm()
    return render(request, "admin_interface/create_artwork.html", {"form": form})


@login_required()
@permission_required("artworks.can_change")
def edit_artwork(request, artwork_id):
    artwork = get_object_or_404(Artwork, id=artwork_id)
    if request.method == "POST":
        form = UpdateForm(request.POST, instance=artwork)
        if form.is_valid():
            form.save()
            messages.success(
                request, "{} a bien été modifié.".format(form.cleaned_data["title"])
            )
            return redirect("view_artworks")
    else:
        form = UpdateForm(instance=artwork)
    return render(request, "admin_interface/edit_artwork.html", {"form": form})


@login_required()
@permission_required("artworks.can_delete")
def delete_artwork(request, artwork_id):
    artwork = get_object_or_404(Artwork, id=artwork_id)

    if request.method == "POST":
        artwork.delete()
        messages.success(request, "{} a bien été supprimé.".format(artwork.title))
        return redirect("view_artworks")

    return render(
        request, "admin_interface/confirm_delete_artwork.html", {"artwork": artwork}
    )


@login_required()
@permission_required("artists.can_view")
def view_artists(request):
    artist_list = Artist.objects.all().order_by("-id")

    paginator = Paginator(artist_list, 4)
    page = request.GET.get("page")
    artists = paginator.get_page(page)

    return render(request, "admin_interface/view_artists.html", {"artists": artists})


@login_required()
@permission_required("artworks.can_add")
def create_artist(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "L'artiste {} a bien été crée.".format(form.cleaned_data["name"]),
            )
            return redirect("view_artists")
    else:
        form = ArtistForm()
    return render(request, "admin_interface/create_artist.html", {"form": form})

@login_required()
@permission_required("artworks.can_change")
def edit_artist(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)


    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            messages.success(request, "L'artiste {} a bien été modifié.".format(form.cleaned_data["name"]))
            return redirect("view_artists")
    else:
        form = ArtistForm(instance=artist)
    return render(request, "admin_interface/edit_artist.html", {"form": form})

@login_required()
@permission_required("artworks.can_delete")
def delete_artist(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)

    if request.method == "POST":
        artist.delete()
        messages.success(
            request, "L'artiste {} a bien été supprimé.".format(artist.name)
        )
        return redirect("view_artists")

    return render(
        request, "admin_interface/confirm_delete_artist.html", {"artist": artist}
    )
