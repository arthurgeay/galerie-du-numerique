from artworks.models import Artwork, Artist, Category
from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView
# Create your views here.
class ArtworkDetailView(DetailView):
    model = Artwork
    queryset = Artwork.objects.filter(id=1)
    print(queryset)
    
    def get(self, request, *args, **kwargs):
        artwork = get_object_or_404(Artwork, id=kwargs['id'])
        context = {'artwork': artwork}
        print(Artwork)
        return render(request, 'artworks/artwork_detail.html', context)
    
    