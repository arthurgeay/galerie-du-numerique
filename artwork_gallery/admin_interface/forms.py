from django import forms

class CreateForm(forms.Form):
    """
    Form for adding the artwork information.
    """
    title = forms.CharField(max_length=100)
    artiste = forms.CharField(max_length=100)
    categorie = forms.CharField()

class UpdateForm(forms.Form):
    """
    Form for updating the artwork information.
    """
    titre = forms.CharField(max_length=100)
    image = forms.CharField(max_length=500)
    artiste = forms.CharField(max_length=100)
    categorie = forms.CharField()
    largeur = forms.IntegerField()
    hauteur = forms.IntegerField()
    lieu = forms.CharField(max_length=100)
    date_realisation = forms.CharField
    description = forms.CharField()

class CreateArtistForm(forms.Form):
    """
    Form for adding the artist information.
    """
    nom = forms.CharField(max_length=100)
    image = forms.CharField(max_length=500)
    date_naissance = forms.CharField()
    date_mort = forms.CharField()