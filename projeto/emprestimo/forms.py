from django import forms
from .models import Emprestimo #, EmprestimoItens
from datetime import date
# from datetimepicker.widgets import DateTimePicker

class EmprestimoForm(forms.ModelForm):    
    class Meta:
        model = Emprestimo        
        fields = [
            'funcionario',
            'num_doc',
            'cliente',
            'valor_emprestado', 
            'qtd_parcelas',
            'valor_prestacao',
            'data_emprestimo'             
        ]
        readonly_fields = ["valor_prestacao", ]
     