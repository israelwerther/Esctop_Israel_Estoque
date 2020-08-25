from django import forms
from .models import Cliente_cnpj


class Cliente_cnpjForm(forms.ModelForm):
    class Meta:
        model = Cliente_cnpj
        fields = '__all__'




