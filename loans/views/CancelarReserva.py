from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from loans.models import Loans
from django.urls import reverse_lazy
from django.contrib import messages

class CancelarReservaView(LoginRequiredMixin, DeleteView):
    model = Loans
    success_url = reverse_lazy("minhas_reservas")
    template_name = "delete.html"

    def get_queryset(self):
        return Loans.objects.filter(aluno=self.request.user)

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(request, 'Cancelamento de Reserva realizado com sucesso!')
        return response