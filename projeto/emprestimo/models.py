from django.contrib.auth.models import User
from django.db import models
from projeto.core.models import TimeStampedModel
from projeto.cliente.models import Cliente


MOVIMENTO = (
    ('r', 'realizar'),
    ('p', 'pagar'),    
)


class Emprestimo(TimeStampedModel):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE)
    num_doc     = models.PositiveIntegerField('Nº Documento', null=True, blank=True)
    movimento   = models.CharField(max_length=1, choices=MOVIMENTO)
    
    class Meta:
        ordering=('-created',) #o sinal de '-' indica que está pegando pelo item mais recente, ou seja, em ordem decrescente
    
    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.num_doc, self.created.strftime('%d-%m-%Y'))       
    
   
class EmprestimoItens(models.Model):
    emprestimo          = models.ForeignKey(Emprestimo, on_delete=models.CASCADE)
    cliente          = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor_emprestado = models.DecimalField("Valor Emprestado", max_digits=10, decimal_places=2)
    juros            = models.DecimalField("Juros", max_digits=10, decimal_places=2)
    
    class Meta:
        ordering=('pk',)
        
        def __str__(self):
            return '{} - {} - {}'.format(self.pk, self.emprestimo.pk, self.cliente.pk) 