from django.forms import ModelForm
from loans.models import Loans
from datetime import datetime


class EmprestimoForm(ModelForm):
    class Meta:
        model = Loans
        fields = ['carregador']


