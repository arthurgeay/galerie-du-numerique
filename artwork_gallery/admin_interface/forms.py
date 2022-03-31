from django import forms

from artworks.models import Artwork
from artworks.models import Artist

class CreateForm(forms.ModelForm):
    """
    Form for adding the artwork information.
    """
    class Meta:
        model = Artwork
        fields = ['title', 'category', 'artist']
        labels = {
            "title": "Titre",
            "category": "Catégorie",
            "artist": "Artiste"
        }

class UpdateForm(forms.ModelForm):
    """
    Form for updating the artwork information.
    """
    class Meta:
        model = Artwork
        fields = ['title', 'description', 'image', 'released_at', 'width', 'height', 'location', 'category', 'artist']
        labels = {
            "title": "Titre",
            "released_at": "Date de réalisation",
            "width": "Largeur",
            "height": "Hauteur",
            "location": "Lieu",
            "category": "Catégorie",
            "artist": "Artiste"
        }

class CreateArtistForm(forms.ModelForm):
    """
    Form for adding the artist information.
    """
    class Meta:
        model = Artist
        fields = ['name', 'image', 'birthday', 'deathday']
        labels = {
            "name": "Nom",
            "birthday": "Date de naissance",
            "deathday": "Date de mort"
        }