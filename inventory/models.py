from django.db import models
from loans.models import Loans


COLORS = [
    ("PRETO", "Preto"), ("CINZA", "Cinza"), 
    ("BRANCO", "Branco"), ("PRATA", "Prata")
]

STATUS = [
    ("DISPONIVEL", "Disponível"),
    ("MANUTENCAO", "Manutenção"),
    ("EMPRESTADO", "Emprestado"),
]
class Brand(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    brand = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.brand
    class Meta:
        verbose_name = 'Marca'



class Notebook(models.Model):
    numero_patrimonio = models.Field(blank=False, max_length=6, unique=True, verbose_name="Nº Patrimônio")
    marca= models.ForeignKey(Brand, on_delete=models.PROTECT)
    cor = models.CharField(max_length=30,  choices=COLORS)
    modelo = models.CharField(max_length=50)
    status = models.CharField(max_length=15, choices=STATUS, default="DISPONIVEL")

    @property
    def aluno_atual(self):
        if self.status == "EMPRESTADO":
            emprestimo = Loans.objects.filter(notebook=self, data_devolucao__isnull=True).last()
            return emprestimo.aluno.first_name if emprestimo else "NÃO IDENTIFICADO"
        return '-'

    def __str__(self):
        return f"{self.numero_patrimonio} - {self.marca}"
    class Meta:
        verbose_name = 'Notebook'


    


