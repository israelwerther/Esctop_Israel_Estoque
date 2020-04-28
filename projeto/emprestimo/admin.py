from django.contrib import admin
from .models import Emprestimo, EmprestimoItens

class EmprestimoItensInline(admin.TabularInline):
    model = EmprestimoItens
    extra = 0
    

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display=(
        '__str__',
        'funcionario',
        'num_doc',
        'movimento',
    )
    inlines = (EmprestimoItensInline,)  
    list_display = ('__str__', 'num_doc', 'funcionario', 'movimento',)  
    search_fields = ('num_doc',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'
    
    