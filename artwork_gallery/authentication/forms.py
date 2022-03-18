from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import PasswordResetForm
class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=63,
        label="",
        widget=forms.TextInput(attrs={"placeholder": _("Nom d'utilisateur")}),
    )
    password = forms.CharField(
        max_length=63,
        widget=forms.PasswordInput(attrs={"placeholder": _('Mot de passe')}),
        label="",
    )


class SignupForm(UserCreationForm):
    username = forms.CharField(label=_("Nom d'utilisateur"))
    email = forms.EmailField(label=_("Adresse e-mail"))
    password1 = forms.CharField(label=_("Mot de passe"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Confirmation du mot de passe"), widget=forms.PasswordInput)
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email", "password1", "password2")
    
class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_('Email'), widget=forms.EmailInput(attrs={
        'type': 'email',
        'name': 'email'
        }))
    
