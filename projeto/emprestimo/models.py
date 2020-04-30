from django.contrib.auth.models import User
from django.db import models
from projeto.cliente.models import Cliente

class Emprestimo(models.Model):
    funcionario      = models.ForeignKey(User, on_delete=models.CASCADE)
    num_doc          = models.PositiveIntegerField('Nº Documento', null=True, blank=True)    
    cliente          = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    valor_emprestado = models.DecimalField("Valor Emprestado", max_digits=10, decimal_places=2, null=True, blank=True)
    qtd_parcelas     = models.PositiveIntegerField('Qtd Parcelas', null=True, blank=True)
    valor_prestacao  = models.DecimalField("Valor da prestação", max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering=('funcionario',)
        
    def __str__(self):
        return self.emprestimo