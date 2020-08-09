from django import forms
from .models import Avalista, Teste


class AvalistaForm(forms.ModelForm):
    class Meta:
        model = Avalista
        fields = '__all__'


class TesteForm(forms.ModelForm):
    class Meta:
        model = Teste
        fields = '__all__'