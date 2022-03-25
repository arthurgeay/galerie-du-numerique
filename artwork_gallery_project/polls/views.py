from django.shortcuts import render, redirect, get_object_or_404

from artworks.models import Artwork
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages


@login_required()
@permission_required("artworks.can_vote")
def add_vote(request, id):

    if request.POST:
        artwork = get_object_or_404(Artwork, pk=id)
        artwork.votes.add(request.user)
        messages.add_message(
            request,
            messages.SUCCESS,
            "Votre vote a bien été pris en compte pour l'oeuvre {}.".format(
                artwork.title
            ),
        )

    return redirect("artwork_detail", id)
