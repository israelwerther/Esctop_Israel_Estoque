from django.contrib import admin
from .models import Cliente_cnpj, Cliente_cnpj_aval

@admin.register(Cliente_cnpj_aval)
class Cliente_cnpj_avalAdmin(admin.ModelAdmin):
    list_display=(        
        'aval_razao_social',
        'aval_nome_fantasia',
        'aval_cnpj',
        
    )
    search_fields=('aval_razao_social',)
    list_filter=('aval_razao_social',)

@admin.register(Cliente_cnpj)
class Cliente_cnpjAdmin(admin.ModelAdmin):
    list_display=(        
        'razao_social',
        'nome_fantasia',
        'cnpj',
        'fundacao',
        'forma_constituicao',
        'inscricao_estadual', 
        'inscricao_municipal',  
    )
    search_fields=('nome_fantasia',)
    list_filter=('email',)


