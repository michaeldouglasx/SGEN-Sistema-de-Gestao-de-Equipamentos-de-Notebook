from django.db import models
from loans.models import Loans
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

STATUS = [
    ("DISPONIVEL", "Disponível"),
    ("MANUTENCAO", "Manutenção"),
    ("EMPRESTADO", "Emprestado"),
]

class Color(models.Model):
    name_color = models.CharField( max_length=40, verbose_name='Nome da cor', unique=True)
    def __str__(self):
        return  self.name_color
    
    def padronizar_cor(self):
        self.name_color = self.name_color.title()
    
    def save(self, *args, **kwargs):
        self.padronizar_cor()
        return super().save(*args, **kwargs)


    
    
    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural= "Cores"



class Brand(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    brand = models.CharField(max_length=50, unique=True)

    def formatar_nome(self):
        self.brand = self.brand.capitalize()

    def save(self, *args, **kwargs):
        self.formatar_nome()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.brand
    class Meta:
        verbose_name = 'Marca'
        verbose_name = 'Marcas'


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

    @classmethod
    def verificar_disponibilidade(cls):
        disponivel = cls.objects.filter(status = 'DISPONIVEL').exists()
        if not disponivel:
            raise ValidationError("Não há notebooks disponíveis no momento!")
        
    def formatar_nome_modelo(self):
        self.modelo = self.modelo.title()

    def save(self, *args, **kwargs ):
        self.formatar_nome_modelo()
        return super().save(*args, **kwargs)
    
    
