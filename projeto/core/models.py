from django.db import models

class TimeStampedModel(models.Model):
    created = models.DateTimeField("criado em", auto_now=True, auto_now_add=False)
    modified = models.DateTimeField("Modificado em", auto_now=False, auto_now_add=True)
    
    class Meta:
        abstract = True


class Banco(models.Model):
    banco         = models.CharField("Banco", max_length=25, blank=True, null=True)   

    class Meta:
        ordering = ('banco',)
    
    def __str__(self):
        return str(self.banco)
        
        
class Tipo_de_conta(models.Model):
    tipo_de_conta = models.CharField("tipo_de_conta", max_length=25, blank=True, null=True)   

    class Meta:
        ordering = ('tipo_de_conta',)
    
    def __str__(self):
        return str(self.tipo_de_conta)


