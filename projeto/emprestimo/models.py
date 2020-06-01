from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy
from projeto.core.models import TimeStampedModel
from projeto.cliente.models import Cliente
from django.utils.translation import gettext_lazy as _ 

import math

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


class EmprestimoPagamento(models.Model):
    emprestimo           = models.ForeignKey(Emprestimo, on_delete=models.PROTECT)
    valor_pago           = models.DecimalField("Valor Pago", max_digits=10, decimal_places=2, null=True, blank=True)
    data_pagamento       = models.DateField("Data do Pagamento", auto_now_add=False, auto_now=False, null=True,blank=True,)

    
    