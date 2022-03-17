from django.shortcuts import render

def gallery(request):
    return render(request, "artworks/index.html", {})