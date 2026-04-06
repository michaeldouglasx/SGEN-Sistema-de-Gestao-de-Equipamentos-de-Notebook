from django.contrib import admin
from .models import Notebook, Brand, Color

@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):

    list_display = ('numero_patrimonio', 'marca',  'modelo', 'cor','status', 'aluno_atual' )
    list_filter = ('status', 'marca')
    search_fields = ('numero_patrimonio',)
    readonly_fields = ('status',)
    



@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand',)
    search_fields = ('brand',)
    list_filter = ('brand',)

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name_color',)
    
    
    
