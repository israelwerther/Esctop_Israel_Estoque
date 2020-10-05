# from django.forms import ModelForm
from django import forms
from .models import Emprestimo, EmprestimoPagamento 
from datetime import date


class EmprestimoForm(forms.ModelForm):    
    class Meta:
        model = Emprestimo        
        fields = [
            'funcionario',            
            'cliente',
            'cliente_cnpj',
            'valor_emprestado', 
            'qtd_parcelas',
            'valor_prestacao',
            'data_emprestimo',
            'data_teste',
            'n_contrato'
        ]
        readonly_fields = ["valor_prestacao", ]


class EmprestimoPagamentoForm(forms.ModelForm):
    class Meta:
        model = EmprestimoPagamento 
        fields = ["valor_pago", "data_pagamento", ]