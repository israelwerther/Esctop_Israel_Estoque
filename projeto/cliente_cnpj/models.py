from django.db import models
from django.urls import reverse_lazy


class Cliente_cnpj(models.Model):
    nome_fantasia         = models.CharField("Nome Fantasia", max_length=50)
    fundacao              = models.DateField("Fundação",max_length=8, blank=True, null=True)  
    forma_constituicao    = models.CharField("Forma Constituição", blank=True, null=True, max_length=50)
    inscricao_estadual    = models.CharField("Inscrição Estadual",blank=True, null=True, max_length=50)
    inscricao_municipal   = models.CharField("Inscrição Municipal", blank=True, null=True,max_length=50)
    email                 = models.EmailField("Email", max_length=50, blank=True, null=True)

    class Meta:
        ordering = ('nome_fantasia',) #confirme se é a organização e apague o coment

    def __str__(self):
        return self.nome_fantasia
    
    def get_absolute_url(self):
        return reverse_lazy('cliente_cnpj:cliente_cnpj_detail', kwargs={'pk': self.pk})