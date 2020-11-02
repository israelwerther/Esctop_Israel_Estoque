# from django.forms import ModelForm
from django import forms
from .models import Emprestimo, EmprestimoPagamento 
from datetime import date


class EmprestimoForm(forms.ModelForm):    
    class Meta:
        created_date = forms.DateField(input_formats=['%d/%m/%Y',],
        widget=forms.DateInput(attrs={'class':'datepicker form-control', 'placeholder':'Select a date'}), required=False)
        model = Emprestimo   
        fields = [
            'funcionario',            
            'cliente',
            'cliente_cnpj',
            'valor_emprestado', 
            'qtd_parcelas',
            'valor_prestacao',            
            'dt_emprestimo',            
            'n_contrato',
            'valor_multa'
        ]
        readonly_fields = ["valor_prestacao", ]
        # widgets = {           
        #     # 'data_emprestimo': forms.DateInput(),
        #     'dt_teste': forms.DateInput(),            
        # }

class EmprestimoPagamentoForm(forms.ModelForm):
    class Meta:
        model = EmprestimoPagamento 
        fields = ["valor_pago", "data_pagamento", ]