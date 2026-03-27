from django.urls import path
from ..views.ReservaView import ReservaView
from ..views.MinhasReservasView import MinhasReservasView


urlpatterns = [
    path('index/', ReservaView.as_view(), name='reserva'),
    path('MinhasReservas/', MinhasReservasView.as_view(), name='minhas_reservas')
]