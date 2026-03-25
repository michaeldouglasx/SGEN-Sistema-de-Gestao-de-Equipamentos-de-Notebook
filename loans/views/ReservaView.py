from django.shortcuts import render

from django.views.generic.edit import CreateView
from loans.forms import EmprestimoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Loans
# @login_required
# def Reserva_View(requests):
#     return render(requests, 'index.html')


class ReservaView(LoginRequiredMixin ,CreateView):
    model = Loans
    fields = ['carregador']
    template_name = 'index.html'


    
        


