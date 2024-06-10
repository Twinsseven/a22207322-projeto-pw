from django.contrib import admin
from .models import Localizacao, Banda, Festival

class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('nome',)
    search_fields = ('nome',)

class BandaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('nome',)
    search_fields = ('nome',)

class FestivalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'localizacao', 'display_bandas', 'imagem_preview')
    ordering = ('nome',)
    search_fields = ('nome',)
    readonly_fields = ('imagem_preview',)

    def display_bandas(self, obj):
        return ", ".join([banda.nome for banda in obj.bandas.all()])

    def imagem_preview(self, obj):
        if obj.imagem:
            return f'<img src="{obj.imagem.url}" style="max-width:100px; max-height:100px;" />'
        else:
            return 'Nenhuma imagem'

    imagem_preview.allow_tags = True
    imagem_preview.short_description = 'Imagem'

admin.site.register(Localizacao, LocalizacaoAdmin)
admin.site.register(Banda, BandaAdmin)
admin.site.register(Festival, FestivalAdmin)
