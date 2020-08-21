from django import forms
from .models import Cliente_cnpj, Cliente_cnpj_aval

class Cliente_cnpj_avalForm(forms.ModelForm):

    class Meta:
        model = Cliente_cnpj_aval
        fields = '__all__'


class Cliente_cnpjForm(forms.ModelForm):

    class Meta:
        model = Cliente_cnpj
        fields = '__all__'




