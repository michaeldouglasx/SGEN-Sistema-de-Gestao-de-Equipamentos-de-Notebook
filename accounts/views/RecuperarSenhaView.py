from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from accounts.forms import RecuperarSenhaForm


class RecuperarSenhaView(FormView):
    template_name = "recuperar_senha.html"
    form_class = RecuperarSenhaForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
  