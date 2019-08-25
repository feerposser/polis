from django.contrib import admin

from .models import ModelContato


class AdminModelContato(admin.ModelAdmin):
    actions = None
    list_display = ('nome', 'email', 'assunto',)
    list_filter = ('nome', 'email', 'assunto')
    search_fields = ['nome', 'email', 'assunto']


admin.site.register(ModelContato, AdminModelContato)