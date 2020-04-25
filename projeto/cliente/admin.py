from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display=(        
        'nome',
        'endereco',
        'rg',
        'data_nasc',
        'anotacoes',
        'email',
        'cpf',
        'num_telefone',        
    )
    search_fields=('nome',)
    list_filter=('rg',)
