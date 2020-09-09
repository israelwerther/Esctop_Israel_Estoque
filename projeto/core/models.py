from django.db import models

class TimeStampedModel(models.Model):
    created = models.DateTimeField("criado em", auto_now=True, auto_now_add=False)
    modified = models.DateTimeField("Modificado em", auto_now=False, auto_now_add=True)
    
    class Meta:
        abstract = True


class Dados_bancarios(models.Model):
    banco         = models.CharField("Banco", max_length=25, blank=True, null=True)
    # n_operacao    = models.CharField("Nº operação", max_length=15, blank=True, null=True)
    # n_agencia     = models.CharField("Nº agência", max_length=15, blank=True, null=True)
    # n_conta       = models.CharField("Nº conta", max_length=15, blank=True, null=True)
    # tipo_conta    = models.CharField("Tipo de conta", max_length=15, blank=True, null=True)
    class Meta:
        ordering = ('banco',)
    
    def __str__(self):
        return str(self.banco)