from django import forms
from .models import Cliente, Avalista

class ClienteForm(forms.ModelForm):
    
    # def existe_cpf(self):
    #     cpf = self.cleaned_data['cpf']
    #     if Cliente.objects.filter(cpf=cpf).exists():
    #         print("CPF já existe")
    #         raise forms.ValidationError('CPF ja cadastrado!')
    #     return cpf    

    class Meta:
        model = Cliente
        fields = '__all__'
        
        
class AvalistaForm(forms.ModelForm):
    class Meta:
        model = Avalista
        fields = '__all__'