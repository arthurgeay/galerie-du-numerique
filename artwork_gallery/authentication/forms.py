from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label="", widget=forms.TextInput(attrs={'placeholder':"Nom d'utilisateur"}))
    password = forms.CharField(max_length=63, widget=forms.PasswordInput(attrs={'placeholder':"Mot de passe"}), label='')