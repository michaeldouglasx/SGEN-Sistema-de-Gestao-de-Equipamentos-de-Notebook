from django.shortcuts import render
from django.views.generic.edit import CreateView
from loans.forms import EmprestimoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Loans
from django.urls import reverse_lazy
from inventory.models import Notebook




class ReservaView(LoginRequiredMixin, CreateView):
    model = Loans
    template_name = 'index.html'
    form_class = EmprestimoForm
    success_url = reverse_lazy('minhas_reservas')
    context_object_name = 'loans'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.instance.aluno = self.request.user
        return form
    
    def form_valid(self, form):
        
        return super().form_valid(form)
    
    
    



    
        


