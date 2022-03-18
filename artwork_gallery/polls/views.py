from django.shortcuts import render, redirect, get_object_or_404

from artworks.models import Artwork
from django.contrib.auth.decorators import login_required, permission_required


@login_required()
@permission_required("artworks.can_vote")
def add_vote(request, id):
    if request.POST:
        artwork = get_object_or_404(Artwork, pk=id)
        artwork.votes.add(request.user)

        # Todo render on artwork details page
        return redirect("gallery")
    else:
        return redirect("gallery")
