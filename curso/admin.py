from django.contrib import admin
from django.utils.html import format_html
from .models import Curso, AreaCientifica, Disciplina, Projeto, LinguagemProgramacao, Docente

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'apresentacao', 'objetivos', 'competencias')
    ordering = ('nome',)
    search_fields = ('nome',)

class AreaCientificaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('nome',)
    search_fields = ('nome',)

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'semestre', 'ects', 'curricular', 'area_cientifica', 'curso')
    ordering = ('nome',)
    search_fields = ('nome',)

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('disciplina', 'descricao', 'conceitos_usados', 'tecnologias_usadas', 'foto', 'video_link', 'github_link')
    ordering = ('disciplina',)
    search_fields = ('disciplina',)

    def foto(self, obj):
        return format_html('<img src="{}" style="width: 75px; height: 75px;" />', obj.imagem.url)
    foto.short_description = 'Imagem'

    def video_link(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.video, obj.video)
    video_link.short_description = 'Vídeo Link'

    def github_link(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.github, obj.github)
    github_link.short_description = 'GitHub Link'

class LinguagemProgramacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('nome',)
    search_fields = ('nome',)

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', )
    ordering = ('nome',)
    search_fields = ('nome',)

admin.site.register(Curso, CursoAdmin)
admin.site.register(AreaCientifica, AreaCientificaAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(LinguagemProgramacao, LinguagemProgramacaoAdmin)
admin.site.register(Docente, DocenteAdmin)