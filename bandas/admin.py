from django.contrib import admin
from django.utils.html import format_html
from .models import Banda, Album, Musica

class BandaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero_membros', 'foto', 'nacionalidade', 'ano_criacao', 'biografia')
    ordering = ('nome',)
    search_fields = ('nome',)

    def foto(self, obj):
        return format_html('<img src="{}" style="width: 75px; height: 75px;" />', obj.foto_Banda.url)
    foto.short_description = 'Foto'

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('banda', 'nome', 'numero_musicas', 'ano_lancamento', 'foto')
    ordering = ('banda',)
    search_fields = ('banda',)

    def foto(self, obj):
        return format_html('<img src="{}" style="width: 75px; height: 75px;" />', obj.capa.url)
    foto.short_description = 'Foto'

class MusicaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'spotify_link', 'duracao', 'letra')
    ordering = ('nome',)
    search_fields = ('nome', 'tipo')

    def spotify_link(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.spotify, obj.spotify)
    spotify_link.short_description = 'Spotify Link'

admin.site.register(Banda, BandaAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Musica, MusicaAdmin)
