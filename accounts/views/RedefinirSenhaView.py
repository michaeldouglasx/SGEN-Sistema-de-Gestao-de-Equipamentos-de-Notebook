from django.views.generic import FormView
from ..forms import RedefinirSenhaForm
from ..models import TokenRecuperacao
from django.shortcuts import get_object_or_404, redirect

from django.urls import reverse_lazy

class RedefinirSenhaView(FormView):
    template_name = 'redefinir-senha.html'
    form_class = RedefinirSenhaForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        codigo_uuid = self.kwargs.get('codigo_token')
        token = get_object_or_404(TokenRecuperacao, codigo = codigo_uuid, usado=False)
        usuario = token.usuario
        nova_senha = form.cleaned_data.get('nova_senha')
        usuario.set_password(nova_senha) 
        usuario.save()
        token.usado = True
        token.save()
        
  
        return super().form_valid(form)



