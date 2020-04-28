from django.contrib import admin
from .models import Emprestimo

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display=(
        '__str__',
        'funcionário',
        'num_doc',
        'movimento',
    )
    search_fields=('num_doc',)
    list_filter=('funcionário',)
    date_hierarchy = 'created'
    
    