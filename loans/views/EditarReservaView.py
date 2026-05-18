from django.views.generic import DetailView
from loans.models import Loans

class EditarReservaView(DetailView):
    model = Loans
    template_name = "editar_reserva.html"
    context_object_name = 'reserva'

    


    