from django.urls import path
from . import views

urlpatterns = [
    path('', views.festivais_views, name='festivais'),
    path('festival/<int:festival_id>/', views.festival_views, name='festival'),
]
