from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Loans(models.Model):
    aluno = models.ForeignKey("accounts.User", on_delete=models.PROTECT, verbose_name="Aluno" )
    notebook = models.ForeignKey("inventory.Notebook", on_delete=models.PROTECT, verbose_name="Notebook")
    carregador = models.BooleanField(default=False)
    data_retirada = models.DateTimeField(auto_now_add=True, verbose_name="Data de Retirada")
    data_devolucao = models.DateTimeField(null=True,blank=True, verbose_name="Data de Devolução")
    horario = models.TimeField(auto_now_add=True, verbose_name='Hora do pedido')
    emprestado = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.aluno}-{self.notebook}"
    
    class Meta:
        verbose_name = 'Empréstimo'

    def save(self, *args, **kwargs):
        self.full_clean()
        if not self.data_devolucao:
            self.notebook.status = 'EMPRESTADO'
        else:
            self.notebook.status = 'DISPONIVEL'
        self.notebook.save()
        super().save(*args, **kwargs)

    def clean(self):
        if not self.pk and self.notebook.status in ["EMPRESTADO", "MANUTENCAO"]:
            raise ValidationError("NOTEBOOK: Notebook não está disponível")
        if not self.pk:
            ja_possui_emprestimo = Loans.objects.filter(aluno=self.aluno, data_devolucao__isnull=True).exists()
            if ja_possui_emprestimo:
                raise ValidationError("ALUNO: Aluno possui empréstimo ativo")
        
        
            
        


        


        
    
