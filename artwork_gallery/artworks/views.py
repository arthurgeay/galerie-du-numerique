from artworks.models import Artwork, Artist, Category
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Artwork


@login_required()
def gallery(request):
    # TODO list by popularity
    artwork_list = Artwork.objects.all()
    categories = Category.objects.all()

    paginator = Paginator(artwork_list, 4)  # Show 4 artworks per page
    page = request.GET.get("page")
    artworks = paginator.get_page(page)

    return render(request, "artworks/index.html", {"artworks": artworks, "categories": categories})


class ArtworkDetailView(DetailView):
    model = Artwork
    queryset = Artwork.objects.filter(id=1)

    def get(self, request, *args, **kwargs):
        artwork = get_object_or_404(Artwork, id=kwargs["id"])
        return render(request, "artworks/artwork_detail.html", {"artwork": artwork})
