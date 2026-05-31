from django.views.generic import UpdateView
from accounts.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class EditarPerfil(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name','last_name','phone']
    template_name = 'editarperfil.html'
    success_url = reverse_lazy ('perfil')

    def form_valid(self, form):
        form.instance.email_academico = self.request.user.email_academico
        return super().form_valid(form)