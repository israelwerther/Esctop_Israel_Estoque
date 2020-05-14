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
        
        
# data_emprestimo = DateField(input_formats=settings.DATE_INPUT_FORMATS)
    # class Meta:
    #     model = Emprestimo
    #     fields = '__all__'   
    # data_emprestimo = DateField(input_formats=['%d-%m-%Y'])       
        
    
# data_emprestimo = forms.DateField()
# widgetwidgets = {
#     'data_emprestimo': forms.DateInput(
#         format=('%d-%m-%Y'), 
#         attrs={'class':'form-control', 
#         'placeholder':'Select a date'}),                 
#     }


# class DateForm(forms.Form):
#     data_emprestimo = forms.DateTimeField(
#         input_formats=['%d-%m-%Y %H:%M'],
#         widget=forms.DateTimeInput(attrs={
#             'class': 'form-control datetimepicker-input',
#             'data-target': '#datetimepicker1'
#         })
#     )


# class EmprestimoItensForm(forms.ModelForm):
#     class Meta:
#         model = EmprestimoItens
#         fields = '__all__'


