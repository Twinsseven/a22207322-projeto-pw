from django.shortcuts import render
from .models import Localizacao, Festival

def festivais_views(request):
    localizacoes = Localizacao.objects.all()
    return render(request, 'festivais/festivais.html', {'localizacoes': localizacoes})

def festival_views(request, festival_id):
    festival = Festival.objects.get(pk=festival_id)
    return render(request, 'festivais/festival.html', {'festival': festival})
