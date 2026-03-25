from django.urls import path
from ..views.ReservaView import ReservaView

urlpatterns = [
    path('index/', ReservaView.as_view(), name='reserva')]