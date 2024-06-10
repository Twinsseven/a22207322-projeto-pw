from django.shortcuts import render, redirect
from django.contrib.auth import models, authenticate, login, logout
from .models import Post, Comentario
from .forms import PostForm, ComentarioForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test

def posts_views(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'artigos/posts.html', context)

def comments_views(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comentarios.all()
    context = {'post': post, 'comments': comments}
    return render(request, 'artigos/comments.html', context)


def group_required(*group_names):
    def in_groups(user):
        if user.is_authenticated:
            if bool(user.groups.filter(name__in=group_names)) | user.is_superuser:
                return True
        raise PermissionDenied
    return user_passes_test(in_groups)

#----------------------------------------------------------------------------------------------CRIAR
@group_required('Editor de Artigos')
def novoPost_view(request):

    form = PostForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('artigos:posts')
    context = {'form': form}
    return render(request, 'artigos/criarPost.html', context)

@group_required('Editor de Artigos')
def novoComment_view(request):
    form = ComentarioForm(request.POST or None, request.FILES)
    if form.is_valid():
        comment = form.save(commit=False)
        post_id = comment.post.id
        comment.save()
        return redirect('artigos:comments', post_id=post_id)
    context = {'form': form}
    return render(request, 'artigos/criarComment.html', context)

#-----------------------------------------------------------------------------------------------EDITAR
@group_required('Editor de Artigos')
def editarPost_view(request, post_id):

    post = Post.objects.get(id=post_id)

    if request.POST:
        form = PostForm(request.POST or None, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('artigos:posts')
    else:
        form = PostForm(instance=post)

    context = {'form': form, 'post': post}
    return render(request, 'artigos/editaPost.html', context)

@group_required('Editor de Artigos')
def editarComment_view(request, comment_id):
    comentario = Comentario.objects.get(id=comment_id)
    post_id = comentario.post.id

    if request.method == "POST":
        form = ComentarioForm(request.POST, request.FILES, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('artigos:comments', post_id=post_id)
    else:
        form = ComentarioForm(instance=comentario)

    context = {'form': form, 'comentario': comentario}
    return render(request, 'artigos/editaComment.html', context)


#---------------------------------------------------------------------------------------------------APAGAR

@group_required('Editor de Artigos')
def apagaPost_view(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('artigos:posts')

@group_required('Editor de Artigos')
def apagaComment_view(request, comment_id):
    comentario = Comentario.objects.get(id=comment_id)
    post_id = comentario.post.id
    comentario.delete()
    return redirect('artigos:comments', post_id=post_id)

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
        return redirect('artigos:login')

    return render(request, 'artigos/registo.html')


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
            return redirect('artigos:posts')
        else:
            render(request, 'artigos/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'artigos/login.html')

#-------------------------------------------------------------------------------------------------------Logout

def logout_view(request):
    logout(request)
    return redirect('artigos:login')

