from django.contrib import admin
from .models import Cliente, Avalista

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display=(        
        'nome',
        'rua',
        'rg',
        'data_nasc',
        'anotacoes',
        'email',        
        'contato1',        
    )
    search_fields=('nome',)
    list_filter=('rg',)
    
    
@admin.register(Avalista)
class AvalistaAdmin(admin.ModelAdmin):
    list_display=(        
        'avalista',
        'cpf_avalista',             
    )
    search_fields=('cpf_avalista',)
    list_filter=('avalista',)
    
