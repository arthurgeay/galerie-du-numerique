from django.shortcuts import render

def presentation(request):
    return render(request, "presentation/index.html", {})

def legacy(request):
    return render(request, "presentation/legacy.html", {})

def agreement(request):
    return render(request, "presentation/agreement.html", {})

def policy(request):
    return render(request, "presentation/policy.html", {})