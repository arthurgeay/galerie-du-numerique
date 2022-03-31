from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.models import Group
from . import forms


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
