from django.views.generic import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from loans.models import Loans
from django.urls import reverse_lazy

class CancelarReservaView(LoginRequiredMixin, UpdateView):
    model = Loans
    success_url = reverse_lazy("minhas_reservas")
    template_name = "delete.html"
    context_object_name = "emprestimo"
    fields = []

    def form_valid(self, form):
        if form.instance.status == 'PENDENTE':
            form.instance.status = 'CANCELADO'
        return super().form_valid(form)

    

    
    


    