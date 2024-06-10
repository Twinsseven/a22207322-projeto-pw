from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('noobsite/', include('noobsite.urls')),
    path('pwsite/', include('pwsite.urls')),
    path('novaapp/', include('novaapp.urls')),
    path('bandas/', include('bandas.urls')),
    path('artigos/', include('artigos.urls')),
    path('curso/', include('curso.urls')),
    path('festivais/', include('festivais.urls')),
    path('meteo/', include('meteo.urls')),
    path('', include('portfolio.urls')),
]