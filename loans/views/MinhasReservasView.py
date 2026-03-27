from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from loans.models import Loans

class MinhasReservasView(LoginRequiredMixin, ListView):
    model = Loans
    template_name = 'meus_emprestimos.html'
    context_object_name = 'reservas'


    def get_queryset(self):
        return Loans.objects.filter(aluno=self.request.user).order_by('-data_retirada')

