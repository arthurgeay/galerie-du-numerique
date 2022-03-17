from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Artwork


@login_required()
def gallery(request):
    # TODO list by popularity
    artworks = Artwork.objects.all()
    return render(request, "artworks/index.html", {'artworks': artworks})