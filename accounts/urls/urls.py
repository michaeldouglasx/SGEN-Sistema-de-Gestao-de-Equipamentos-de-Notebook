from django.urls import path
from ..views.LoginView import Login_View
from ..views.CadastroView import Cadastro_View
from ..views.LogoutView import Logout_View
from ..views.RecuperarSenhaView import RecuperarSenhaView
from ..views.RedefinirSenhaView import RedefinirSenhaView
from accounts.views.PerfilView import PerfilView
from accounts.views.EditarPerfil import EditarPerfil

urlpatterns = [
    path('login/', Login_View, name='login'),
    path('cadastro/', Cadastro_View, name='cadastro'),
    path('logout/', Logout_View, name='logout'),
    path('forgot-password', RecuperarSenhaView.as_view(), name='recuperar_senha'),
    path('redefinir-senha/<uuid:codigo_token>/', RedefinirSenhaView.as_view(), name='redefinir_senha'),
    path('perfil/', PerfilView.as_view(), name='perfil'),
    path('perfil/editar/<int:pk>', EditarPerfil.as_view(), name='editar_perfil')

]
