from django.urls import path
from ..views.ReservaView import ReservaView
from ..views.MinhasReservasView import MinhasReservasView
from ..views.CancelarReserva import CancelarReservaView 


urlpatterns = [
    path('index/', ReservaView.as_view(), name='reserva'),
    path('MinhasReservas/', MinhasReservasView.as_view(), name='minhas_reservas'),
    path('CancelarReserva/<int:pk>', CancelarReservaView.as_view(), name='cancelar_reserva')


]