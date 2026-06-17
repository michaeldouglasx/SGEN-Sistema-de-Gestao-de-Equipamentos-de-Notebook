from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login


def Login_View(request):

    if request.user.is_authenticated:
        return redirect('reserva') 
    
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)

        if login_form.is_valid():

            user = login_form.get_user()

            if not user.is_active:
                login_form.add_error(
                    None,
                    "Sua conta não está ativa"
                )
                return render(
                    request,
                    'login.html',
                    {'login_form': login_form}
                )

            login(request, user)

            if user.profile == 1 or user.is_superuser:
                return redirect('admin:index')

            return redirect('reserva')

        login_form.add_error(
            None,
            'Usuário ou senha inválidos!'
        )

    else:
        login_form = AuthenticationForm()
        login_form.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Digite seu e-mail'
        })

        login_form.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Digite sua senha'
        })

    return render(
        request,
        'login.html',
        {'login_form': login_form}
    )
        
                                  























  





