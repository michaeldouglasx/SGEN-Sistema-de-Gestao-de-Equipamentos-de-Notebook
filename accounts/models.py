from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid

class User(AbstractUser):
    id = models.BigAutoField(primary_key=True, null=False)
    first_name = models.CharField(max_length=150, blank=True, verbose_name="Nome")
    last_name = models.CharField(max_length=150, blank=True, verbose_name="Sobrenome")
    email_academico = models.EmailField( max_length=150, blank=False, verbose_name="E-mail Acadêmico", help_text="Example: aluno@edu.df.senac.br")
    phone = models.CharField(blank=False, max_length= 15, help_text="Formato (61) 9 9888-7777", verbose_name="Telefone de contato" )

    
    def __str__(self):
        return f"{self.first_name}"
    
class TokenRecuperacao(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    codigo = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    usado = models.BooleanField(default=False)

    def __str__(self):
        return f'Token de {self.usuario.email_academico}'

