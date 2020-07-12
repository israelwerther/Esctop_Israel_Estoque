from django.db import models
from django.urls import reverse_lazy

class Avalista(models.Model):
    avalista                   = models.CharField("Avalista", max_length=50, blank=True, null=True)
    cpf_avalista               = models.CharField("CPF do Avalista", max_length=20, unique=True)
    rg_avalista                = models.CharField("RG",max_length=20, blank=True, null=True)
    orgao_expedidor_avalista   = models.CharField("Org Exp", max_length=15, blank=True, null=True)
    data_nasc_avalista         = models.DateField("Data de Nascimento",max_length=8, blank=True, null=True)   
    naturalidade_avalista      = models.CharField("naturalidade", max_length=15, blank=True, null=True)    
    estado_civil_avalista      = models.CharField("Estado Civil", max_length=15, blank=True, null=True) 
    cep                        = models.CharField("CEP", max_length=10, blank=True, null=True)
    rua                        = models.CharField("Rua", max_length=60, blank=True, null=True)
    bairro                     = models.CharField("Bairro", max_length=40, blank=True, null=True)
    cidade                     = models.CharField("Cidade", max_length=40, blank=True, null=True)
    uf                         = models.CharField("Estado", max_length=2, blank=True, null=True)   
    numero_casa                = models.CharField("Nº ", max_length=5, blank=True, null=True)
        
    class Meta:
        ordering = ('avalista',) 
    
    def __str__(self):
        return self.avalista
    
    def get_absolute_url(self):
        return reverse_lazy('avalista:avalista_add', kwargs={'pk': self.pk})  