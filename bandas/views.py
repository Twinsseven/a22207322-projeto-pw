from django.shortcuts import render, redirect
from django.contrib.auth import models, authenticate, login, logout
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test
from .models import Banda, Album, Musica
from .forms import BandaForm, AlbumForm, MusicaForm

def bandas_view(request):
    bandas = Banda.objects.all()
    context = {'bandas': bandas}
    return render(request, "bandas/bandas.html", context)

def banda_album_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    albums = banda.albuns.all()
    context = {'banda': banda, 'albums': albums}
    return render(request, "bandas/bandaAlbum.html", context)

def album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    musicas = album.musicas.all()
    context = {'album': album, 'musicas': musicas}
    return render(request, "bandas/album.html", context)

def musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    album = musica.album
    context = {'musica': musica, 'album': album}
    return render(request, "bandas/musica.html", context)

def group_required(*group_names):
    def in_groups(user):
        if user.is_authenticated:
            if bool(user.groups.filter(name__in=group_names)) | user.is_superuser:
                return True
        raise PermissionDenied
    return user_passes_test(in_groups)

#----------------------------------------------------------------------------------------------CRIAR
@group_required('Editor de Bandas')
def novaBanda_view(request):

    form = BandaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bandas:bandas')
    context = {'form': form}
    return render(request, 'bandas/criarBanda.html', context)

@group_required('Editor de Bandas')
def novoAlbum_view(request):

    form = AlbumForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bandas:bandas')
    context = {'form': form}
    return render(request, 'bandas/criarAlbum.html', context)

@group_required('Editor de Bandas')
def novaMusica_view(request):

    form = MusicaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bandas:bandas')
    context = {'form': form}
    return render(request, 'bandas/criarMusica.html', context)

#-----------------------------------------------------------------------------------------------EDITAR
@group_required('Editor de Bandas')
def editarBanda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)

    if request.POST:
        form = BandaForm(request.POST or None, request.FILES, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('bandas:bandas')
    else:
        form = BandaForm(instance=banda)

    context = {'form': form, 'banda': banda}
    return render(request, 'bandas/editaBanda.html', context)

@group_required('Editor de Bandas')
def editarAlbum_view(request, album_id):
    album = Album.objects.get(id=album_id)

    if request.POST:
        form = AlbumForm(request.POST or None, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('bandas:bandas')
    else:
        form = AlbumForm(instance=album)

    context = {'form': form, 'album': album}
    return render(request, 'bandas/editaAlbum.html', context)

@group_required('Editor de Bandas')
def editarMusica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)

    if request.POST:
        form = MusicaForm(request.POST or None, request.FILES, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('bandas:bandas')
    else:
        form = MusicaForm(instance=musica)

    context = {'form': form, 'musica': musica}
    return render(request, 'bandas/editaMusica.html', context)

#---------------------------------------------------------------------------------------------------APAGAR

@group_required('Editor de Bandas')
def apagaBanda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    banda.delete()
    return redirect('bandas:bandas')
@group_required('Editor de Bandas')
def apagaAlbum_view(request, album_id):
    album = Album.objects.get(id=album_id)
    album.delete()
    return redirect('bandas:bandas')
@group_required('Editor de Bandas')
def apagaMusica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    musica.delete()
    return redirect('bandas:bandas')

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
        return redirect('bandas:login')

    return render(request, 'bandas/registo.html')


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
            return redirect('bandas:bandas')
        else:
            render(request, 'bandas/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'bandas/login.html')

#-------------------------------------------------------------------------------------------------------Logout

def logout_view(request):
    logout(request)
    return redirect('bandas:login')
