from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy
from projeto.core.models import TimeStampedModel
from projeto.cliente.models import Cliente

import math

#from datetime import datetime, date, timedelta

#analize se é possivel modificar o tamanho das inputs de uma {{ form.as_p }} apenas no model
class Emprestimo(models.Model):
    funcionario      = models.ForeignKey(User, on_delete=models.CASCADE)
    cliente          = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    num_doc          = models.PositiveIntegerField('Nº Documento', null=True, blank=True)    
    valor_emprestado = models.DecimalField("Valor Emprestado", max_digits=10, decimal_places=2, null=True, blank=True)
    qtd_parcelas     = models.PositiveIntegerField('Qtd Parcelas', null=True, blank=True)
    valor_prestacao  = models.DecimalField("Valor da prestação", max_digits=10, decimal_places=2, null=True, blank=True)
    data_emprestimo  = models.DateField("Data do Emprestimo", auto_now_add=False, auto_now=False, null=True,blank=True,)      

    class Meta:
        ordering = ('-data_emprestimo',)
        
    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.num_doc, self.created.strftime('%d-%m-%Y'))
        
    def __str__(self):
        return str(self.num_doc)
    
    def get_absolute_url(self):
        return reverse_lazy('emprestimo:emprestimo_detail', kwargs={'pk': self.pk})  




    
    