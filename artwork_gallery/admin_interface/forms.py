from django import forms

from artworks.models import Artwork

class CreateForm(forms.Form):
    """
    Form for adding the artwork information.
    """
    title = forms.CharField(max_length=100)
    artiste = forms.CharField(max_length=100)
    categorie = forms.CharField()

class UpdateForm(forms.ModelForm):
    """
    Form for updating the artwork information.
    """
    class Meta:
        model = Artwork
        fields = '__all__'

class CreateArtistForm(forms.Form):
    """
    Form for adding the artist information.
    """
    nom = forms.CharField(max_length=100)
    image = forms.CharField(max_length=500)
    date_naissance = forms.CharField()
    date_mort = forms.CharField()