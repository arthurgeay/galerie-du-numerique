from artworks.models import Artwork, Artist, Category
from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView
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

@login_required()
class ArtworkDetailView(DetailView):
    model = Artwork
    queryset = Artwork.objects.filter(id=1)
    
    def get(self, request, *args, **kwargs):
        artwork = get_object_or_404(Artwork, id=kwargs['id'])
        artist = Artist.objects.get(id=artwork.artist_id)
        category = Category.objects.get(id=artwork.category_id)
        context = {'artwork': artwork, 'artist': artist, 'category': category}
        return render(request, 'artworks/artwork_detail.html', context)
