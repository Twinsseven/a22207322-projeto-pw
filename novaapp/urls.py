from django.urls import path
from . import views

app_name = 'novaapp'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('paris/', views.paris, name='paris'),
    path('toquio/', views.toquio, name='toquio'),
]