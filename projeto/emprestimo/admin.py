from django.contrib import admin
from .models import Emprestimo
    

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    # list_display = ('__str__', 'num_doc', 'funcionario', 'movimento',)  
    search_fields = ('num_doc',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'
    
    