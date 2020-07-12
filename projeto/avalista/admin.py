from django.contrib import admin
from .models import Avalista

@admin.register(Avalista)
class AvalistaAdmin(admin.ModelAdmin):
    list_display=(        
        'avalista',
        'cpf_avalista',             
    )
    search_fields=('cpf_avalista',)
    list_filter=('avalista',)
