from django.contrib import admin
from .models import User, Turma
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class UserPersonalizadoAdmin(UserAdmin):
    list_display = ('first_name', 'email_academico', 'phone', 'is_active', 'profile' )
    search_fields = ('first_name', 'email_academico', 'phone','is_active')
    list_per_page = 30
    fieldsets =  (
    (
        'Informações Acadêmicas',
        {
            'fields': (
                'first_name',
                'email_academico',
                'phone',
                'turma',
            )
        },
        
    ), ('Geral', {
            'fields':(
                'is_active',
                'profile',

            )
        })
)
    add_fieldsets =  (
    (
        'Informações Acadêmicas',
        {
            'fields': (
                'first_name',
                'last_name',
                'email_academico',
                'phone',
                'turma',
            )
        },
        
    ),('Geral', {
            'fields':(
                'is_active',
                'profile',

            )
        })
)

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'semestre', 'turno' )
    search_fields = ('nome', 'semestre', 'turno')
    list_per_page = 30
    
