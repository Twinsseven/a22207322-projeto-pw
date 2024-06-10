from django.urls import path
from . import views

app_name = 'bandas'

urlpatterns = [
    path('', views.bandas_view, name='bandas'),
    path('banda/<int:banda_id>/', views.banda_album_view, name='bandaAlbum'),
    path('album/<int:album_id>/', views.album_view, name='album'),
    path('musica/<int:musica_id>/', views.musica_view, name='musica'),

    path('banda/novaBanda', views.novaBanda_view, name="criaBanda"),
    path('album/novoAlbum', views.novoAlbum_view, name="criaAlbum"),
    path('musica/novaMusica', views.novaMusica_view, name="criaMusica"),

    path('banda/<int:banda_id>/edita', views.editarBanda_view,name="editaBanda"),
    path('album/<int:album_id>/edita', views.editarAlbum_view,name="editaAlbum"),
    path('musica/<int:musica_id>/edita', views.editarMusica_view,name="editaMusica"),

    path('banda/<int:banda_id>/apaga', views.apagaBanda_view,name="apagaBanda"),
    path('album/<int:album_id>/apaga', views.apagaAlbum_view,name="apagaAlbum"),
    path('musica/<int:musica_id>/apaga', views.apagaMusica_view,name="apagaMusica"),

    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]
