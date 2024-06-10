from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.posts_views, name='posts'),
    path('artigos/<int:post_id>/', views.comments_views, name='comments'),

    path('artigos/novoPost', views.novoPost_view, name="criaPost"),
    path('comentario/novoComment/', views.novoComment_view, name="criaComment"),

    path('artigos/<int:post_id>/edita/', views.editarPost_view, name="editaPost"),
    path('comentario/<int:comment_id>/edita/', views.editarComment_view, name="editaComment"),

    path('artigos/<int:post_id>/apaga/', views.apagaPost_view, name="apagaPost"),
    path('comentario/<int:comment_id>/apaga/', views.apagaComment_view, name="apagaComment"),

    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]
