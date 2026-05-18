from django.views.generic import TemplateView
from accounts.models import User

class PerfilView(TemplateView):
    template_name = 'perfil.html'
    