from django.contrib import admin
from .models import Loans



@admin.register(Loans)
class LoansAdmin(admin.ModelAdmin):
    
    list_display = ('aluno', 'data_retirada', 'horario', 'notebook', 'emprestado')
    

    list_filter = ('emprestado', 'data_retirada')
    
    
    search_fields = ('aluno__first_name', 'aluno__username')

    
    fieldsets = (
        ('Informações do Aluno', {
            'fields': ('aluno', 'carregador')
        }),
        ('Aprovação Técnica', {
            'fields': ('notebook', 'emprestado', 'data_devolucao')
        }),
    )

    
    readonly_fields = ('aluno', 'carregador', 'status')


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "notebook":
            
            kwargs["queryset"] = db_field.related_model.objects.filter(status='DISPONIVEL')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    
    def status_pedido(self, obj):
        if obj.emprestado:
            return "Aprovado"
        return "Pendente"
    status_pedido.short_description = 'Status'