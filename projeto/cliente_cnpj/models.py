from django.db import models
from django.urls import reverse_lazy
from projeto.cliente.models import Cliente

class Cliente_cnpj(models.Model):
    razao_social          = models.CharField("Razão Social", max_length=50, blank=True, null=True)
    nome_fantasia         = models.CharField("Nome Fantasia", max_length=50)
    cnpj                  = models.CharField("CNPJ", max_length=36, unique=True, blank=True, null=True)
    fundacao              = models.DateField("Fundação",max_length=8, blank=True, null=True)  
    forma_constituicao    = models.CharField("Forma Constituição", blank=True, null=True, max_length=50)
    inscricao_estadual    = models.CharField("Inscrição Estadual",blank=True, null=True, max_length=50)
    inscricao_municipal   = models.CharField("Inscrição Municipal", blank=True, null=True,max_length=50)
    email                 = models.EmailField("Email", max_length=50, blank=True, null=True)

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

    agencia               = models.CharField("Agência",max_length=15, blank=True, null=True)
    conta                 = models.CharField("Conta",max_length=15, blank=True, null=True)
    banco                 = models.CharField("Banco",max_length=25, blank=True, null=True)
    obs_bancaria          = models.CharField("Observações",max_length=25, blank=True, null=True)    

    representante         = models.ForeignKey(Cliente,on_delete=models.PROTECT, max_length=11, blank=True, null=True)

    anotacoes             = models.TextField("Anotações",max_length=200, blank=True, null=True)

    class Meta:
        ordering = ('nome_fantasia',)
        
    def __str__(self):
        return self.nome_fantasia
    
    def get_absolute_url(self):
        return reverse_lazy('cliente_cnpj:cliente_cnpj_detail', kwargs={'pk': self.pk})