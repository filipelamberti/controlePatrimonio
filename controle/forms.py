from django import forms
from controle.models import Controle

class PatrimonioForm(forms.Form):
    nome = forms.CharField(max_length='50', required=True)
    descricao = forms.CharField(max_length='100', required=True)
    valor = forms.CharField(max_length='10', required=True)
    status = forms.CharField(max_length='1', blank=True)
    