from django.contrib import admin
from .models import Emprestimo, EmprestimoPagamento

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display=(        
        'data_emprestimo',        
    )
    search_fields=('num_doc',)
    # readonly_fields = ["valor_prestacao", ]
    # list_filter=('rg',)
    
@admin.register(EmprestimoPagamento)
class EmprestimoPagamentoAdmin(admin.ModelAdmin):
    list_display=(        
        'valor_pago',        
    )
    