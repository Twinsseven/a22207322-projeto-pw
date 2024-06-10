from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.landing_page, name='landing-page'),
    path('mebyme/', views.mebyme, name='mebyme'),
    path('sobre/', views.sobre, name='sobre'),
]
