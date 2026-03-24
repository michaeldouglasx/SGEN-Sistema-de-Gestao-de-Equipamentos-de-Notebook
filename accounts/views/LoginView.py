from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login


def Login_View(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request,user)

            url_destino = 'admin:index' if user.is_superuser else 'reserva'
            return redirect(url_destino)
        
        login_form.errors.clear()
        login_form.add_error(None, 'Usuário ou senha inválidos!')
    else:
            login_form = AuthenticationForm()

    return render(request, 'login.html', {'login_form': login_form})





