from django.views.generic import UpdateView
from loans.models import Loans
from loans.forms import EmprestimoForm
from django.urls import reverse_lazy

class AtualizarReservaView(UpdateView):
    model = Loans
    context_object_name = 'reserva'
    template_name = 'atualizar_reserva.html'
    form_class = EmprestimoForm
    success_url = reverse_lazy('minhas_reservas') 

  
