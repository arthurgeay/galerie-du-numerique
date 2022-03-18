from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Artwork

@login_required()
def gallery(request):
    # TODO list by popularity
    artwork_list = Artwork.objects.all()

    paginator = Paginator(artwork_list, 6)  # Show 6 artworks per page
    page = request.GET.get("page")
    artworks = paginator.get_page(page)

    return render(request, "artworks/index.html", {"artworks": artworks})
