from django.db import models
from loans.models import Loans
from django.core.validators import MaxValueValidator, MinValueValidator



STATUS = [
    ("DISPONIVEL", "Disponível"),
    ("MANUTENCAO", "Manutenção"),
    ("EMPRESTADO", "Emprestado"),
]


class Color(models.Model):
    name_color = models.CharField( max_length=40, verbose_name='Nome da cor', unique=True)
    def __str__(self):
        return  self.name_color
    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural= "Cores"

class Brand(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    brand = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.brand
    class Meta:
        verbose_name = 'Marca'



class Notebook(models.Model):
    numero_patrimonio = models.IntegerField(blank=False, unique=True, verbose_name="Nº Patrimônio", validators=[
            MinValueValidator(100000),
            MaxValueValidator(999999) ])
    marca= models.ForeignKey(Brand, on_delete=models.PROTECT,  )
    cor = models.ForeignKey(Color, on_delete=models.PROTECT)
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
        


    


