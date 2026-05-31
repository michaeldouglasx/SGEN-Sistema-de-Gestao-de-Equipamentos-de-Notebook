from django.views.generic import UpdateView
from loans.models import Loans
from loans.forms import EmprestimoForm
from django.urls import reverse_lazy
from django.contrib import messages

class AtualizarReservaView(UpdateView):
    model = Loans
    context_object_name = 'reserva'
    template_name = 'atualizar_reserva.html'
    form_class = EmprestimoForm
    success_url = reverse_lazy('minhas_reservas')

    def form_valid(self, form):
        if form.instance.status == "CANCELADO":
            return self.form_invalid(form)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Essa reserva já está cancelada ou não pode ser cancelada.')
        return super().form_invalid(form)
    


