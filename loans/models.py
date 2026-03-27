from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import time

class Loans(models.Model):
    aluno = models.ForeignKey("accounts.User", on_delete=models.PROTECT, verbose_name="Aluno" )
    notebook = models.ForeignKey("inventory.Notebook", on_delete=models.PROTECT, null=True, blank=True)
    carregador = models.BooleanField(default=False)
    data_retirada = models.DateTimeField(auto_now_add=True, verbose_name="Data de Retirada")
    data_devolucao = models.DateTimeField(null=True,blank=True, verbose_name="Data de Devolução")
    horario = models.TimeField(auto_now_add=True, verbose_name='Hora do pedido')
    emprestado = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.aluno}-{self.notebook}"
    
    class Meta:
        verbose_name = 'Empréstimo'

    def esta_na_janela_retirada(self, hora):
            return time(14, 0) <= hora <= time(15, 20)

    def esta_na_janela_devolucao(self, hora):
            return time(21, 40) <= hora <= time(22, 0)



    def clean(self):
        agora = timezone.localtime().replace(second=0, microsecond=0).time()


        if not self.pk:
            if not self.esta_na_janela_retirada(agora):
                raise ValidationError("Fora do horário de RETIRADA (19:00 - 19:20)")


        if self.data_devolucao and self.emprestado:
            if not self.esta_na_janela_devolucao(agora):
                raise ValidationError("Fora do horário de DEVOLUÇÃO (21:40 - 22:00)")



    def save(self, *args, **kwargs):
            self.full_clean()


            if self.notebook and self.emprestado:

                self.atualizar_status_inventario()

            super().save(*args, **kwargs)

    def atualizar_status_inventario(self):

        if self.data_devolucao:
            self.notebook.status = 'DISPONIVEL'
        else:
            self.notebook.status = 'EMPRESTADO'
            self.notebook.save()




        
            
        
        
        
        
        
            
        


        


        
    
