from django.shortcuts import render, redirect
from django.contrib.auth import models, authenticate, login, logout
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test
from .models import Curso, Disciplina, Projeto, Docente
from .forms import DisciplinaForm, ProjetoForm, DocenteForm
from django.http import Http404



def curso_views(request):
    curso = Curso.objects.first()
    context = {'curso': curso}
    return render(request, "curso/curso.html", context)

def disciplina_views(request):
    disciplinas = Disciplina.objects.all().order_by('nome')
    context = {'disciplina': disciplinas}
    return render(request, "curso/disciplina.html", context)

def disciplina_detail_view(request, disciplina_id):
    try:
        disciplina = Disciplina.objects.get(id=disciplina_id)
        return render(request, 'curso/disciplina_detail.html', {'disciplina': disciplina})
    except Disciplina.DoesNotExist:
        raise Http404("Disciplina não encontrada")


def projeto_detail_view(request, projeto_id):
    try:
        projeto = Projeto.objects.get(id=projeto_id)
        return render(request, 'curso/projeto.html', {'projeto': projeto})
    except Projeto.DoesNotExist:
        raise Http404("Projeto não encontrado")


def group_required(*group_names):
    def in_groups(user):
        if user.is_authenticated:
            if bool(user.groups.filter(name__in=group_names)) | user.is_superuser:
                return True
        raise PermissionDenied
    return user_passes_test(in_groups)

#----------------------------------------------------------------------------------------------CRIAR
@group_required('Editor de Curso')
def novaDisciplina_view(request):

    form = DisciplinaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('curso:curso')
    context = {'form': form}
    return render(request, 'curso/criarDisciplina.html', context)

@group_required('Editor de Curso')
def novoProjeto_view(request):

    form = ProjetoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('curso:curso')
    context = {'form': form}
    return render(request, 'curso/criarProjeto.html', context)

@group_required('Editor de Curso')
def novoDocente_view(request):

    form = DocenteForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('curso:curso')
    context = {'form': form}
    return render(request, 'curso/criarDocente.html', context)

#-----------------------------------------------------------------------------------------------EDITAR
@group_required('Editor de Curso')
def editarDisciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)

    if request.POST:
        form = DisciplinaForm(request.POST or None, request.FILES, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('curso:curso')
    else:
        form = DisciplinaForm(instance=disciplina)

    context = {'form': form, 'disciplina': disciplina}
    return render(request, 'curso/editaDisciplina.html', context)

@group_required('Editor de Curso')
def editarProjeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)

    if request.POST:
        form = ProjetoForm(request.POST or None, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('curso:curso')
    else:
        form = ProjetoForm(instance=projeto)

    context = {'form': form, 'projeto': projeto}
    return render(request, 'curso/editaProjeto.html', context)

@group_required('Editor de Curso')
def editarDocente_view(request, docente_id):
    docente = Docente.objects.get(id=docente_id)

    if request.POST:
        form = DocenteForm(request.POST or None, request.FILES, instance=docente)
        if form.is_valid():
            form.save()
            return redirect('curso:curso')
    else:
        form = DocenteForm(instance=docente)

    context = {'form': form, 'docente': docente}
    return render(request, 'curso/editaDocente.html', context)

#---------------------------------------------------------------------------------------------------APAGAR

@group_required('Editor de Curso')
def apagaDisciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    disciplina.delete()
    return redirect('curso:curso')
@group_required('Editor de Curso')
def apagaProjeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()
    return redirect('curso:curso')
@group_required('Editor de Curso')
def apagaDocente_view(request, docente_id):
    docente = Docente.objects.get(id=docente_id)
    docente.delete()
    return redirect('curso:curso')

#-----------------------------------------------------------------------------------------------------Registo

def registo_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('curso:login')

    return render(request, 'curso/registo.html')


#------------------------------------------------------------------------------------------------------Login

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('curso:curso')
        else:
            render(request, 'curso/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'curso/login.html')

#-------------------------------------------------------------------------------------------------------Logout

def logout_view(request):
    logout(request)
    return redirect('curso:login')


