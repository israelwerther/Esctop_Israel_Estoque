from django.contrib import admin
from .models import Emprestimo

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display=(        
        'funcionario',        
    )
    search_fields=('nome',)
    # list_filter=('rg',)