from django.contrib import admin

from .models import Receita


@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('name', 'preparationtime', 'like', 'deslike')
    search_fields = ('name', 'ingredients')
