from django.urls import path
from . import views

app_name = 'curso'

urlpatterns = [
    path('', views.curso_views, name='curso'),
    path('disciplina/', views.disciplina_views, name='disciplina'),
    path('disciplina/<int:disciplina_id>/', views.disciplina_detail_view, name='disciplinaDetalhe'),
    path('projeto/<int:projeto_id>/', views.projeto_detail_view, name='projeto'),

    path('disciplina/novaDisciplina', views.novaDisciplina_view, name="criaDisciplina"),
    path('projeto/novoProjeto', views.novoProjeto_view, name="criaProjeto"),
    path('docente/novoDocente', views.novoDocente_view, name="criaDocente"),

    path('disciplina/<int:disciplina_id>/edita', views.editarDisciplina_view,name="editaDisciplina"),
    path('projeto/<int:projeto_id>/edita', views.editarProjeto_view,name="editaProjeto"),
    path('docente/<int:docente_id>/edita', views.editarDocente_view,name="editaDocente"),

    path('disciplina/<int:disciplina_id>/apaga', views.apagaDisciplina_view,name="apagaDisciplina"),
    path('projeto/<int:projeto_id>/apaga', views.apagaProjeto_view,name="apagaProjeto"),
    path('docente/<int:docente_id>/apaga', views.apagaDocente_view,name="apagaDocente"),

    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]