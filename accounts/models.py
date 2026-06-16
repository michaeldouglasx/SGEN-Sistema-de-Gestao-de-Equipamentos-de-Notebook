from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid

PROFILE = ((1, "ADMIN"),
           (2, 'PROFESSOR'),
           (3, 'ALUNO'),
           (4, "NÃO ATRIBUIDO"))

DIAS_DA_SEMANA = ((0, "Segunda-Feira"),
                (1, 'Terça-Feira'),
                (2, "Quarta-Feira"),
                (3, 'Quinta-Feira'),
                (4, "Sexta-Feira"),
                (5, 'Sábado'),
                (6, "Domingo")
                 )

SEMESTRES = (
    (1, "Primeiro"),
    (2, "Segundo"),
)

class Turma(models.Model):
    codigo = models.UUIDField(default=uuid.uuid4, primary_key=False, editable=False, unique=True)
    nome = models.CharField(max_length=30, blank=False, null=False)
    semestre = models.IntegerField(choices=SEMESTRES)
    turno = models.CharField(choices=(('Matutino', 'Matutino'),
                                      ('Vespertino', 'Vespertino'),
                                        ('Noturno', 'Noturno')),
                                          max_length=30)
    
    dia_da_semana = models.IntegerField(choices=DIAS_DA_SEMANA)
    horario_inicial = models.TimeField()
    horario_final = models.TimeField()
    ano = models.PositiveSmallIntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"


class User(AbstractUser):
    first_name = models.CharField(max_length=150, blank=True, verbose_name="Nome")
    last_name = models.CharField(max_length=150, blank=True, verbose_name="Sobrenome")
    email_academico = models.EmailField(unique=True, max_length=150, blank=False, verbose_name="E-mail Acadêmico", help_text="Example: aluno@edu.df.senac.br")
    phone = models.CharField(blank=False, max_length= 15, help_text="Formato (61) 9 9888-7777", verbose_name="Telefone de contato" )
    profile = models.IntegerField(choices=PROFILE, default= 4 )
    turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True, blank= True, related_name="usuarios")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
    
class TokenRecuperacao(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    codigo = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    usado = models.BooleanField(default=False)

    def __str__(self):
        return f'Token de {self.usuario.email_academico}'