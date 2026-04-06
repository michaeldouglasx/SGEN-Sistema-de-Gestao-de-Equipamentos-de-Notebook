from django.forms import ModelForm
from loans.models import Loans



class EmprestimoForm(ModelForm):
    class Meta:
        model = Loans
        fields = ['carregador']


