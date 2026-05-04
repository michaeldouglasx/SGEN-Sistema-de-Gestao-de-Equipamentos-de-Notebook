from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from loans.models import Loans
from django.urls import reverse_lazy
from django.contrib import messages

class DetalheEmprestimoView(LoginRequiredMixin, DetailView):
    model = Loans
    
