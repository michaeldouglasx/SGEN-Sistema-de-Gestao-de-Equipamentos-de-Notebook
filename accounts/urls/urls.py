from django.urls import path
from ..views.LoginView import Login_View
from ..views.CadastroView import Cadastro_View
from ..views.ReservaView import Reserva_View
from ..views.LogoutView import Logout_View
from ..views.RecuperarSenhaView import RecuperarSenhaView


urlpatterns = [
    path('login/', Login_View, name='login'),
    path('cadastro/', Cadastro_View, name='cadastro'),
    path('reserva/', Reserva_View, name='reserva'),
    path('logout/', Logout_View, name='logout'),
    path('forgot-password', RecuperarSenhaView.as_view(), name='recuperar_senha')

]
