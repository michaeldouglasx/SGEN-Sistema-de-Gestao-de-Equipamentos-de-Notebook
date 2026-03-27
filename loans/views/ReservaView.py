from django.shortcuts import render
from django.views.generic.edit import CreateView
from loans.forms import EmprestimoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Loans
from django.urls import reverse_lazy




class ReservaView(LoginRequiredMixin, CreateView):
    model = Loans
    template_name = 'index.html'
    form_class = EmprestimoForm
    success_url = reverse_lazy('reserva')

    def form_valid(self, form):
        form.instance.aluno = self.request.user
        print(form.instance)
        return super().form_valid(form)
    



    
        


