from django.forms import ModelForm
from django import forms
from accounts.models import User, TokenRecuperacao


class CadastroForm(forms.Form):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email_academico = forms.EmailField(max_length=150)
    phone = forms.CharField(max_length=15)
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Crie sua Senha",
        min_length=8
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirme sua senha",
        min_length=8)

    def save(self):
        user = User(
            first_name = self.cleaned_data.get('first_name'),
            last_name = self.cleaned_data.get('last_name'),
            email_academico = self.cleaned_data.get('email_academico'),
            phone = self.cleaned_data.get('phone'),
            username = self.cleaned_data.get('email_academico')

        )

        user.is_staff = False
        user.is_active = False
        

        senha = self.cleaned_data.get("password")
        user.set_password(senha)
        user.save()
        return user

        
    
    def clean_email_academico(self):
        email = self.cleaned_data.get('email_academico')
        if User.objects.filter(email_academico=email).exists():
            raise forms.ValidationError('Este e-mail já está cadastrado no SGEN')
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        senha_digitada = self.cleaned_data.get("password")
        confirmacao_de_senha_digitada = self.cleaned_data.get("confirm_password")

        if senha_digitada != confirmacao_de_senha_digitada:
            raise forms.ValidationError("Senhas não são idênticas")
        else:
            return cleaned_data
        

class RecuperarSenhaForm(ModelForm):
    class Meta:
        model = User
        fields = ['email_academico']

    def clean_email_academico(self):
        email = self.cleaned_data.get('email_academico')
        if not User.objects.filter(email_academico=email).exists():
            raise forms.ValidationError("E-mail não cadastrado!")
        return email
    
    def save(self):
        email = self.cleaned_data.get('email_academico')
        usuario = User.objects.get(email_academico=email)
        token = TokenRecuperacao.objects.create(usuario=usuario)
        return token
    

class RedefinirSenhaForm(forms.Form):
    nova_senha = forms.CharField(widget=forms.PasswordInput, label= 'Nova Senha', min_length=8)
    confirmacao_senha = forms.CharField(widget=forms.PasswordInput, label= 'Digite a senha novamente', min_length=8)

    def clean(self):
        senha = self.cleaned_data.get('nova_senha')
        self.validar_senha(senha)
        confirmar = self.cleaned_data.get('confirmacao_senha')
        if senha != confirmar:
            raise forms.ValidationError("Senhas não são identicas")
        return self.cleaned_data
    
    def validar_senha(self, senha):
        if not senha:
            return
        tamanho = len(senha)
        if tamanho < 8:
            raise forms.ValidationError("Senha: A senha cadastrada possui menos de 8 caracteres")