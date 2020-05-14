from django.contrib import admin
from .models import Emprestimo

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display=(        
        'data_emprestimo',        
    )
    search_fields=('num_doc',)
    # list_filter=('rg',)