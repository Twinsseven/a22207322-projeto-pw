from django import forms
from .models import Post, Comentario

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class ComentarioForm(forms.ModelForm):
  class Meta:
    model = Comentario
    fields = '__all__'