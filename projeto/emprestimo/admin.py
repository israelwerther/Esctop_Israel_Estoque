from django.contrib import admin
from .models import Emprestimo, EmprestimoPagamento

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display=(        
        'num_doc', 'cliente', 'data_emprestimo', 'funcionario', 'valor_emprestado',        
    )
    search_fields=('num_doc',)
    # readonly_fields = ["valor_prestacao", ]
    # list_filter=('rg',)   
    ordering = ('-num_doc',)
    
@admin.register(EmprestimoPagamento)
class EmprestimoPagamentoAdmin(admin.ModelAdmin):
    list_display=(        
        'valor_pago', 'data_pagamento', 'emprestimo',       
    )
    ordering = ('-data_pagamento',)
    