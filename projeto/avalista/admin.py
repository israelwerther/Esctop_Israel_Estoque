from django.contrib import admin
from .models import Avalista, Teste

@admin.register(Avalista)
class AvalistaAdmin(admin.ModelAdmin):
    list_display=(        
        'fiador_nome',
        'fiador_cpf',             
    )
    search_fields=('fiador_nome',)
    list_filter=('fiador_cpf',)
    

@admin.register(Teste)
class AvalistaAdmin(admin.ModelAdmin):
    list_display=(        
        'teste',
        'cpf_teste',             
    )    
