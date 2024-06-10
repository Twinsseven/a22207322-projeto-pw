from django.urls import path
from . import views

app_name = 'meteo'

urlpatterns = [
    path('', views.tempo_lisboa, name='tempo_lisboa'),
    path('previsao-tempo/', views.previsao_tempo, name='previsao_tempo'),
    path('api/cidades', views.lista_cidades, name='lista_cidades'),
    path('api/previsao/hoje', views.previsao_hoje, name='previsao_hoje'),
    path('api/previsao/5dias', views.previsao_5dias, name='previsao_5dias'),
    path('documentacao/', views.api_documentacao, name='api_documentacao'),
]
