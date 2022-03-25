from django import forms

class CreateForm(forms.Form):
    """
    Form for updating the artwork information.
    """
    title = forms.CharField(max_length=100)
    artiste = forms.CharField(max_length=100)
    categorie = forms.CharField()