import requests
from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse

def tempo_lisboa(request):
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
        'cidade': 'Lisboa',
        'temp_min': previsao_hoje['tMin'],
        'temp_max': previsao_hoje['tMax'],
        'data': previsao_hoje['forecastDate'],
        'icone': f'/static/meteo/icons/{icone}'
    }
    return render(request, 'meteo/tempo_lisboa.html', context)


def obter_distritos():
    url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    distritos = [(distrito['globalIdLocal'], distrito['local']) for distrito in data['data']]
    return distritos

def previsao_tempo(request):
    distritos = obter_distritos()
    cidade_selecionada = request.GET.get('cidade')

    if cidade_selecionada:
        cidade_id = cidade_selecionada
    else:
        cidade_id = 1110600  # Lisboa por padrão

    previsao = consultar_previsao(cidade_id)
    return render(request, 'meteo/previsao_tempo.html', {'previsao': previsao, 'distritos': distritos, 'cidade_selecionada': cidade_selecionada})


def consultar_previsao(cidade_id):
    url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{cidade_id}.json'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    previsao = []
    for dia in data['data']:
        data_previsao = dia['forecastDate']
        temp_min = dia['tMin']
        temp_max = dia['tMax']
        descricao = dia['predWindDir']

        weather_type = dia['idWeatherType']
        hora_atual = datetime.now().hour
        if 6 <= hora_atual < 20:
            icone = f'w_ic_d_{weather_type:02}anim.svg'
        else:
            icone = f'w_ic_n_{weather_type:02}anim.svg'

        previsao.append({
            'data': data_previsao,
            'temp_min': temp_min,
            'temp_max': temp_max,
            'descricao': descricao,
            'icone': f'/static/meteo/icons/{icone}'
        })

    return previsao

#------------------------------------------------------------------------------------------------------API METEO-----------------------------------------------------------------------------------------------

CIDADES = {
    "Lisboa": 1110600,
    "Porto": 1131200,
    "Madrid": 1234567,  # Substituir por IDs reais
    "Paris": 2345678    # Substituir por IDs reais
}

def lista_cidades(request):
    return JsonResponse({"cidades": list(CIDADES.keys())})

def previsao_hoje(request):
    cidade = request.GET.get('cidade')
    if not cidade or cidade not in CIDADES:
        return JsonResponse({"erro": "Cidade não encontrada ou não especificada."}, status=400)

    cidade_id = CIDADES[cidade]
    url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{cidade_id}.json'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    if 'data' not in data:
        return JsonResponse({"erro": "Resposta inesperada da API do IPMA."}, status=500)

    previsao_hoje = data['data'][0]
    weather_type = previsao_hoje['idWeatherType']
    hora_atual = datetime.now().hour

    if 6 <= hora_atual < 20:
        icone = f'w_ic_d_{weather_type:02}anim.svg'
    else:
        icone = f'w_ic_n_{weather_type:02}anim.svg'

    return JsonResponse({
        'nome': cidade,
        'temp_min': previsao_hoje['tMin'],
        'temp_max': previsao_hoje['tMax'],
        'data': previsao_hoje['forecastDate'],
        'descricao': previsao_hoje['predWindDir'],
        'precipitacao': previsao_hoje.get('precipitaProb', 'N/A'),
        'icone': f'/static/meteo/icons/{icone}'
    })

def previsao_5dias(request):
    cidade = request.GET.get('cidade')
    if not cidade or cidade not in CIDADES:
        return JsonResponse({"erro": "Cidade não encontrada ou não especificada."}, status=400)

    cidade_id = CIDADES[cidade]
    url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{cidade_id}.json'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    if 'data' not in data:
        return JsonResponse({"erro": "Resposta inesperada da API do IPMA."}, status=500)

    previsoes = []
    for dia in data['data'][:5]:
        weather_type = dia['idWeatherType']
        hora_atual = datetime.now().hour
        if 6 <= hora_atual < 20:
            icone = f'w_ic_d_{weather_type:02}anim.svg'
        else:
            icone = f'w_ic_n_{weather_type:02}anim.svg'

        previsoes.append({
            'data': dia['forecastDate'],
            'temp_min': dia['tMin'],
            'temp_max': dia['tMax'],
            'descricao': dia['predWindDir'],
            'precipitacao': dia.get('precipitaProb', 'N/A'),
            'icone': f'/static/meteo/icons/{icone}'
        })

    return JsonResponse({'nome': cidade, 'previsoes': previsoes})

def api_documentacao(request):
    return render(request, 'meteo/api_documentacao.html')