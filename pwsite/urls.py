from django.urls import path
from . import views

app_name = 'pwsite'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('sobre/', views.index_view1, name='sobre'),
    path('interesses/', views.index_view2, name='interesses'),
]