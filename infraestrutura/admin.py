from django.contrib import admin

from .models import ModelOcorrenciaCategoria, ModelOcorrencia, ModelComentario


class AdminModelOcorrencia(admin.ModelAdmin):
    actions = None
    list_display = ('usuario', 'categoria', 'setor', 'status', 'criacao', 'alteracao')
    list_filter = ('usuario', 'categoria')
    search_fields = ['usuario', 'categoria', 'setor', 'status', 'criacao']


class AdminModelOcorrenciaCategoria(admin.ModelAdmin):
    actions = None
    list_display = ('nome', 'criacao')
    list_filter = ('nome',)
    search_fields = ['nome', 'descricao', 'criacao']


class AdminComentario(admin.ModelAdmin):
    list_display = ('usuario', 'comentario', 'criacao')
    list_filter = ('usuario', 'criacao')
    search_fields = ('usuario', 'comentario', 'criacao', 'estado')

admin.site.register(ModelOcorrencia, AdminModelOcorrencia)
admin.site.register(ModelOcorrenciaCategoria, AdminModelOcorrenciaCategoria)
admin.site.register(ModelComentario, AdminComentario)
