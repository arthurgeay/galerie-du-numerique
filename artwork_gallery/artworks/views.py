from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required()
def gallery(request):
    return render(request, "artworks/index.html", {})