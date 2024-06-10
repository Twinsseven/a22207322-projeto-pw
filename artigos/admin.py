from django.contrib import admin
from .models import Post, Comentario

class PostAdmin(admin.ModelAdmin):
    list_display = ('autor', 'titulo', 'texto', 'data')
    ordering = ('autor',)
    search_fields = ('autor',)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('autor', 'texto', 'rating')
    ordering = ('autor',)
    search_fields = ('autor',)

admin.site.register(Post, PostAdmin)
admin.site.register(Comentario, ComentarioAdmin)