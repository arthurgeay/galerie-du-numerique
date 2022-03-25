from artworks.models import Artwork, Artist, Category
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Artwork


@login_required()
def gallery(request):
    # TODO list by popularity
    artwork_list = Artwork.objects.all()

    paginator = Paginator(artwork_list, 4)  # Show 4 artworks per page
    page = request.GET.get("page")
    artworks = paginator.get_page(page)

    return render(request, "artworks/index.html", {"artworks": artworks})


@login_required()
def artwork_detail(request, id):
    artwork = get_object_or_404(Artwork, id=id)
    is_already_voted = request.user in artwork.votes.all()
    return render(
        request,
        "artworks/artwork_detail.html",
        {"artwork": artwork, "is_already_voted": is_already_voted},
    )
