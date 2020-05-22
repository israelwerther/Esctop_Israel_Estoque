from django.db import models
from django.urls import reverse_lazy

# class CPF(models.Model):
#     cpf             = models.CharField("CPF", max_length=11, blank=True, null=True)
#     data_exp        = models.DateTimeField("Data de expedição", auto_now=False, auto_now_add=False)
    
#     def __str__(self):
#         return self.cpf

#para campo required
#https://stackoverflow.com/questions/1134667/django-required-field-in-model-form/1429646
class Cliente(models.Model):
    nome              = models.CharField("Nome", max_length=50)
    cpf               = models.CharField("CPF", max_length=20, unique=True)   
    rg                = models.CharField("RG",max_length=20, blank=True, null=True)
    data_nasc         = models.DateField("Data de Nascimento",max_length=8, blank=True, null=True)   
    naturalidade      = models.CharField("naturalidade", max_length=15, blank=True, null=True)
    nome_da_mae       = models.CharField("Nome da Mãe", max_length=50, blank=True, null=True)
    nome_do_pai       = models.CharField("Nome da Pai", max_length=50, blank=True, null=True)
    rua               = models.CharField("Rua", max_length=50, blank=True, null=True)
    numero_casa       = models.CharField("Nº ", max_length=5, blank=True, null=True)
    bairro            = models.CharField("Bairro", max_length=50, blank=True, null=True)
    cidade            = models.CharField("Cidade", max_length=50, blank=True, null=True)
    cep               = models.CharField("CEP", max_length=100, blank=True, null=True)
    ponto_referencia  = models.CharField("Ponto de Referencia", max_length=100, blank=True, null=True)
    contato1          = models.CharField("Contato 1",max_length=11, blank=True, null=True)
    contato2          = models.CharField("Contato 2",max_length=11, blank=True, null=True)
    celular1          = models.CharField("celular 1",max_length=11, blank=True, null=True)
    celular2          = models.CharField("celular 2",max_length=11, blank=True, null=True)
    sacado            = models.CharField("Sacado",max_length=50, blank=True, null=True)
    anotacoes         = models.TextField("Anotações",max_length=200)
    email             = models.EmailField("Email", max_length=50, blank=True, null=True)
    
    class Meta:
        ordering = ('nome',) #confirme se é a organização e apague o coment

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse_lazy('cliente:cliente_detail', kwargs={'pk': self.pk})
