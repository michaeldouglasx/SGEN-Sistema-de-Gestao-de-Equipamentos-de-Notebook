from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from accounts.forms import RecuperarSenhaForm
from django.core.mail import send_mail
from SGEN import settings



class RecuperarSenhaView(FormView):
    template_name = "recuperar_senha.html"
    form_class = RecuperarSenhaForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        token_criado = form.save() 

        url_recuperacao = f'http://127.0.0.1:8000/redefinir-senha/{token_criado.codigo}/'
        

        send_mail(
            subject="Recuperação de senha - SGEN",
            message=f"Olá! Clique no link para redefinir sua senha: {url_recuperacao}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[form.cleaned_data.get('email_academico')],
        )

        
        return super().form_valid(form)


        
    
  