from django import forms
from controle.models import Controle

class PatrimonioForm(forms.ModelForm):
    class Meta:
        model = Controle
        