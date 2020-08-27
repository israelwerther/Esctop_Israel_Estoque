from django.db import models
from django.urls import reverse_lazy
from projeto.cliente.models import Cliente
from projeto.avalista.models import Avalista


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
    celular1              = models.CharField("Celular 1",max_length=17, blank=True, null=True)
    celular2              = models.CharField("Celular 2",max_length=17, blank=True, null=True)
    agencia               = models.CharField("Agência",max_length=15, blank=True, null=True)
    conta                 = models.CharField("Conta",max_length=15, blank=True, null=True)
    banco                 = models.CharField("Banco",max_length=25, blank=True, null=True)
    obs_bancaria          = models.CharField("Observações",max_length=25, blank=True, null=True) 

    # REFERÊNCIAS
    ref1_nome             = models.CharField("Nome", max_length=50, blank=True, null=True)
    ref1_contato          = models.CharField("Contato",max_length=17, blank=True, null=True)
    ref1_parentesco       = models.CharField("Parentesco", max_length=50, blank=True, null=True)
    ref2_nome             = models.CharField("Nome", max_length=50, blank=True, null=True)
    ref2_contato          = models.CharField("Contato",max_length=17, blank=True, null=True)
    ref2_parentesco       = models.CharField("Parentesco", max_length=50, blank=True, null=True)

    rep_nome              = models.CharField("Nome", max_length=50, blank=True, null=True)
    rep_cpf               = models.CharField("CPF", max_length=20, unique=True, blank=True, null=True) 
    rep_rg                = models.CharField("RG",max_length=20, blank=True, null=True)
    rep_email             = models.EmailField("Email", max_length=50, blank=True, null=True)
    rep_contato1          = models.CharField("Contato 1",max_length=15, blank=True, null=True)
    rep_celular1          = models.CharField("celular 1",max_length=17, blank=True, null=True)
    rep_celular2          = models.CharField("celular 2",max_length=17, blank=True, null=True)
    rep_cep               = models.CharField("CEP", max_length=10, blank=True, null=True)
    rep_rua               = models.CharField("Rua", max_length=60, blank=True, null=True)
    rep_bairro            = models.CharField("Bairro", max_length=40, blank=True, null=True)
    rep_cidade            = models.CharField("Cidade", max_length=40, blank=True, null=True)
    rep_uf                = models.CharField("Estado", max_length=2, blank=True, null=True)   
    rep_numero_casa       = models.CharField("Nº ", max_length=5, blank=True, null=True)
    rep_ponto_referencia  = models.CharField("Ponto de Referencia", max_length=100, blank=True, null=True)  

    fiador                = models.ForeignKey(Avalista, on_delete=models.CASCADE, blank=True, null=True)

    

    class Meta:
        ordering = ('razao_social',)
        
    def __str__(self):
        return self.razao_social
    
    def get_absolute_url(self):
        return reverse_lazy('cliente_cnpj:cliente_cnpj_detail', kwargs={'pk': self.pk})


# CRIAR UM TEMPLATE PRA RECEBER ESTES DOIS JÁ SALVOS
