from django.db import models
from django.urls import reverse_lazy


class Cliente_cnpj(models.Model):
    nome_fantasia         = models.CharField("Nome Fantasia", max_length=50)
    fundacao              = models.DateField("Fundação",max_length=8, blank=False, null=True)  
    forma_constituicao    = models.CharField("Forma Constituição", max_length=50)
    inscricao_estadual    = models.CharField("Inscrição Estadual", max_length=50)
    inscricao_municipal   = models.CharField("Inscrição Municipal", max_length=50)
    email                 = models.EmailField("Email", max_length=50, blank=True, null=True)