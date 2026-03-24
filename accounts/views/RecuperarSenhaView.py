from django.shortcuts import render
from django.views.generic import View


class RecuperarSenhaView(View):
    def get(self, request):
        return render(request, 'recuperar_senha.html')
        
    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

