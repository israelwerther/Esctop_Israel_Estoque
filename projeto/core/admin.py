from django.contrib import admin
from .models import Dados_bancarios

@admin.register(Dados_bancarios)
class Dados_bancariosAdmin(admin.ModelAdmin):
    list_display=(        
        'banco',
        
    )
    search_fields=('banco',)
    list_filter=('banco',)
