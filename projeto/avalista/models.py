from django.db import models
from django.urls import reverse_lazy

class Avalista(models.Model): 
    fiador_nome                = models.CharField("Nome", max_length=50, blank=True, null=True)
    fiador_cpf                 = models.CharField("CPF", max_length=20, unique=True, blank=True, null=True) 
    fiador_rg                  = models.CharField("RG",max_length=20, blank=True, null=True)
    fiador_org_emissor         = models.CharField("Orgão Emissor",max_length=20, blank=True, null=True)
    fiador_email               = models.EmailField("Email", max_length=50, blank=True, null=True)
    fiador_contato1            = models.CharField("Contato 1",max_length=15, blank=True, null=True)
    fiador_celular1            = models.CharField("celular 1",max_length=17, blank=True, null=True)
    fiador_celular2            = models.CharField("celular 2",max_length=17, blank=True, null=True)
    fiador_cep                 = models.CharField("CEP", max_length=10, blank=True, null=True)
    fiador_rua                 = models.CharField("Rua", max_length=60, blank=True, null=True)
    fiador_bairro              = models.CharField("Bairro", max_length=40, blank=True, null=True)
    fiador_cidade              = models.CharField("Cidade", max_length=40, blank=True, null=True)
    fiador_uf                  = models.CharField("Estado", max_length=2, blank=True, null=True)   
    fiador_numero_casa         = models.CharField("Nº ", max_length=5, blank=True, null=True)
    fiador_ponto_referencia    = models.CharField("Ponto de Referencia", max_length=100, blank=True, null=True)
    fiador_agencia             = models.CharField("Agência",max_length=15, blank=True, null=True)
    fiador_conta               = models.CharField("Conta",max_length=15, blank=True, null=True)
    fiador_banco               = models.CharField("Banco",max_length=25, blank=True, null=True)
    fiador_obs_bancaria        = models.CharField("Observações",max_length=25, blank=True, null=True)
        
    class Meta:
        ordering = ('fiador_nome',) 
    
    def __str__(self):
        return str(self.fiador_nome)
    
    def get_absolute_url(self):
        return reverse_lazy('avalista:avalista_cadastra', kwargs={'pk': self.pk})  
