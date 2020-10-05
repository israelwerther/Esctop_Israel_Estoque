from django.contrib import admin
from .models import Emprestimo, EmprestimoPagamento

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display=(        
        'n_contrato', 'cliente', 'cliente_cnpj', 'data_emprestimo', 'funcionario', 'valor_emprestado',        
    )
    search_fields=('n_contrato',)
    # readonly_fields = ["valor_prestacao", ]
    # list_filter=('rg',)   
    ordering = ('-n_contrato',)
    
@admin.register(EmprestimoPagamento)
class EmprestimoPagamentoAdmin(admin.ModelAdmin):
    list_display=(        
        'valor_pago', 'data_pagamento', 'emprestimo',       
    )
    ordering = ('-data_pagamento',)
    