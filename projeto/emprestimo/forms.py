from django import forms
from .models import Emprestimo#, EmprestimoItens


class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = '__all__'
        

# class EmprestimoItensForm(forms.ModelForm):
#     class Meta:
#         model = EmprestimoItens
#         fields = '__all__'


