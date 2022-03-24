from artworks.models import Artwork, Artist, Category
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from .models import Artwork


@login_required()
def gallery(request):
    # TODO list by popularity
    filter_category = request.GET.get('category')
    artwork_list = Artwork.objects.annotate(votes_count=Count('votes')).order_by('-votes_count').all()
    categories = Category.objects.all()
    if filter_category:
        artwork_list = artwork_list.filter(category=filter_category).order_by('votes').all()

    paginator = Paginator(artwork_list, 4)  # Show 4 artworks per page
    page = request.GET.get("page")
    artworks = paginator.get_page(page)

    return render(request, "artworks/index.html", {"artworks": artworks, "categories": categories})


def filter(request):
    return render(request, "artworks/index.html", {"artworks": artworks, "categories": categories})


class ArtworkDetailView(DetailView):
    model = Artwork
    queryset = Artwork.objects.filter(id=1)

    def get(self, request, *args, **kwargs):
        artwork = get_object_or_404(Artwork, id=kwargs["id"])
        return render(request, "artworks/artwork_detail.html", {"artwork": artwork})
