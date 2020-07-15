from django.contrib import admin
from .models import Cliente_cnpj

@admin.register(Cliente_cnpj)
class Cliente_cnpjAdmin(admin.ModelAdmin):
    list_display=(        
        'nome_fantasia',
        'fundacao',
        'forma_constituicao',
        'inscricao_estadual',
        'inscricao_municipal',
        'email', 
        'cep',  
        'rua',  
        'bairro',  
        'cidade',  
        'uf',  
        'numero_casa',  
        'ponto_referencia',  
    )
    search_fields=('nome_fantasia',)
    list_filter=('email',)


