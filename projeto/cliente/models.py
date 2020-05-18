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
    nome            = models.CharField("Nome", max_length=100)
    endereco        = models.CharField("Endereço", max_length=200, blank=True, null=True)
    rg              = models.CharField("RG",max_length=20, blank=True, null=True)
    data_nasc       = models.DateField("Data de Nascimento",max_length=20, blank=True, null=True)    
    anotacoes       = models.TextField("Anotações",max_length=100, blank=True, null=True)
    email           = models.EmailField("Email", max_length=50, blank=True, null=True)
    cpf             = models.CharField("CPF", max_length=20, unique=True)   
    num_telefone    = models.CharField("Telefone",max_length=20, blank=True, null=True) 
    
    class Meta:
        ordering = ('nome',) #confirme se é a organização e apague o coment

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse_lazy('cliente:cliente_detail', kwargs={'pk': self.pk})
