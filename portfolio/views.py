import requests
from django.shortcuts import render
from datetime import datetime


def landing_page(request):
    url = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    response = requests.get(url)
    response.raise_for_status()
    weather_data = response.json()

    if 'data' not in weather_data:
        raise ValueError("A resposta da API não contém a chave 'data' esperada")

    previsao_hoje = weather_data['data'][0]
    weather_type = previsao_hoje['idWeatherType']

    hora_atual = datetime.now().hour

    if 6 <= hora_atual < 20:
        icone = f'w_ic_d_{weather_type:02}anim.svg'
    else:
        icone = f'w_ic_n_{weather_type:02}anim.svg'

    context = {
        'icone': f'/static/meteo/icons/{icone}'
    }
    return render(request, 'portfolio/landing_page.html', context)


def mebyme(request):
    return render(request, 'portfolio/mebyme.html')

def sobre(request):
    return render(request, 'portfolio/sobre.html')

