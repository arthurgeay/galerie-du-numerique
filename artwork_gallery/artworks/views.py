from artworks.models import Artwork, Artist, Category
from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView
# Create your views here.
class ArtworkDetailView(DetailView):
    model = Artwork
    queryset = Artwork.objects.filter(id=1)
    
    def get(self, request, *args, **kwargs):
        artwork = get_object_or_404(Artwork, id=kwargs['id'])
        artist = Artist.objects.get(id=artwork.artist_id)
        category = Category.objects.get(id=artwork.category_id)
        context = {'artwork': artwork, 'artist': artist, 'category': category}
        print(artist)
        return render(request, 'artworks/artwork_detail.html', context)
    
    