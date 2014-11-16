from django import forms
from controle.models import Controle

class PatrimonioForm(forms.Form):
    class Meta:
        model = Controle
        
    