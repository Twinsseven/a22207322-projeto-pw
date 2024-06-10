from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")
    
def index_view1(request):
    return HttpResponse("O GUI TÁ A TROLLAR")

def index_view2(request):
    return HttpResponse("PARA DE JOGAR DE SKARNER")
    
def index_view3(request):
    return HttpResponse("ACR É MAU NO JOGO")
    
    
