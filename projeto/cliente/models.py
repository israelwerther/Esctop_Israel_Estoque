#para campo required
#https://stackoverflow.com/questions/1134667/django-required-field-in-model-form/1429646
from django.db import models
from django.urls import reverse_lazy
from projeto.avalista.models import Avalista

class Cliente(models.Model):
    nome                  = models.CharField("Nome", max_length=50)
    cpf                   = models.CharField("CPF", max_length=20, unique=True)   
    rg                    = models.CharField("RG",max_length=20, blank=False, null=True)
    orgao_expedidor       = models.CharField("Org Exp", max_length=15, blank=False, null=True)
    data_nasc             = models.DateField("Data de Nascimento",max_length=8, blank=False, null=True)   
    naturalidade          = models.CharField("naturalidade", max_length=15, blank=False, null=True)    
    estado_civil          = models.CharField("Estado Civil", max_length=15, blank=False, null=True)    
    nome_da_mae           = models.CharField("Nome da Mãe", max_length=50, blank=False, null=True)
    nome_do_pai           = models.CharField("Nome da Pai", max_length=50, blank=True, null=True)
    cep                   = models.CharField("CEP", max_length=10, blank=False, null=True)
    rua                   = models.CharField("Rua", max_length=60, blank=False, null=True)
    bairro                = models.CharField("Bairro", max_length=40, blank=False, null=True)
    cidade                = models.CharField("Cidade", max_length=40, blank=False, null=True)
    uf                    = models.CharField("Estado", max_length=2, blank=False, null=True)   
    numero_casa           = models.CharField("Nº ", max_length=5, blank=False, null=True)
    ponto_referencia      = models.CharField("Ponto de Referencia", max_length=100, blank=True, null=True)
    contato1              = models.CharField("Contato 1",max_length=15, blank=True, null=True)
    contato2              = models.CharField("Contato 2",max_length=15, blank=True, null=True)
    celular1              = models.CharField("celular 1",max_length=17, blank=True, null=True)
    celular2              = models.CharField("celular 2",max_length=17, blank=True, null=True)
    sacado                = models.CharField("Sacado",max_length=50, blank=True, null=True)
    email                 = models.EmailField("Email", max_length=50, blank=True, null=True)    
    nome_fantasia         = models.CharField("Nome Fantasia",max_length=50, blank=True, null=True)
    contato1_trabalho     = models.CharField("Contato 1",max_length=15, blank=True, null=True)
    contato2_trabalho     = models.CharField("Contato 2",max_length=15, blank=True, null=True)
    celular1_trabalho     = models.CharField("celular 1",max_length=17, blank=True, null=True)
    celular2_trabalho     = models.CharField("celular 2",max_length=17, blank=True, null=True)
    cep_trabalho          = models.CharField("CEP", max_length=10, blank=True, null=True)
    rua_trabalho          = models.CharField("Rua", max_length=60, blank=True, null=True)
    bairro_trabalho       = models.CharField("Bairro", max_length=40, blank=True, null=True)
    cidade_trabalho       = models.CharField("Cidade", max_length=40, blank=True, null=True)
    uf_trabalho           = models.CharField("Estado", max_length=2, blank=True, null=True)
    referencia_trabalho   = models.CharField("Referência",max_length=50, blank=True, null=True)    
    agencia               = models.CharField("Agência",max_length=15, blank=True, null=True)
    conta                 = models.CharField("Conta",max_length=15, blank=True, null=True)
    banco                 = models.CharField("Banco",max_length=25, blank=True, null=True)
    obs_bancaria          = models.CharField("Observações",max_length=25, blank=True, null=True)    
    avalista              = models.ForeignKey(Avalista,on_delete=models.PROTECT, max_length=11, blank=True, null=True)    
    anotacoes             = models.TextField("Anotações",max_length=200, blank=True, null=True)
    
    class Meta:
        ordering = ('nome',) #confirme se é a organização e apague o coment

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse_lazy('cliente:cliente_detail', kwargs={'pk': self.pk})
