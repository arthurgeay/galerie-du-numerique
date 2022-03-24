from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from . import forms


def login_page(request):
    form = forms.LoginForm()
    message = ""
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                message = _("Bonjour, {}! Vous êtes connecté").format(user.username)
                return redirect("galery")
            else:
                message = _("Identifiants invalides")
    return render(
        request, "authentication/login.html", {"form": form, "message": message}
    )


def logout_user(request):
    logout(request)
    return redirect("login")


def signup_page(request):
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Add user in customers group with can_vote permission
            customers_group = Group.objects.get(name="customers")
            customers_group.user_set.add(user)

            login(request, user)
            return redirect("gallery")
    return render(request, "authentication/signup.html", {"form": form})
