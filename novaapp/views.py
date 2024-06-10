from django.shortcuts import render

def index(request):
    return render(request, "novaapp/index.html")

def paris(request):
    return render(request, "novaapp/paris.html")

def toquio(request):
    return render(request, "novaapp/toquio.html")