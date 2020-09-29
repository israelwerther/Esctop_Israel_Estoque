# IsraelEstoque
Repositório de suporte e aprendizado para outro projeto

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv.
* Ative o virtualenv.
* Instale as dependencias.
* Rode as migrações.

```
git clone https://github.com/israelwerther/Esctop_Israel_Estoque.git
cd Esctop_Israel_Estoque
virtualenv --python=python3 venv
source venv/bin/activate
pip install -r requirements-dev.txt
python contrib/env_gen.py    (cria arquivo .env aleatoriamento toda vez que roda o comando)
python manage.py migrate
```

## Links

[python-decouple](https://github.com/henriquebastos/python-decouple)

[package-of-the-week-python-decouple](https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html)

[github.com/rg3915/tutoriais django-basic](https://github.com/rg3915/tutoriais/tree/master/django-basic)

[bootstrap starter-template](https://getbootstrap.com/docs/4.4/getting-started/introduction/#starter-template)

[emmet](https://emmet.io/)

[start.html](https://github.com/JTruax/bootstrap-starter-template/blob/master/template/start.html)

[django-widget-tweaks](https://github.com/jazzband/django-widget-tweaks)

[Class Based View - ccbv.co.uk](https://ccbv.co.uk/)

[form-inline](http://felipefrizzo.github.io/post/form-inline/)

[form-inline-cbv](http://felipefrizzo.github.io/post/form-inline-cbv/)

[django-bootstrap-form](https://django-bootstrap-form.readthedocs.io/en/latest/)


## PARA ESTUDO 
[configurações do django admin](https://books.agiliq.com/projects/django-admin-cookbook/en/latest/introduction.html)

## OBSERVAÇÕES

<!-- PENDENCIAS -->
* (OK) CORRIGIR O ESPAÇO DA PROMISSÓRIA NO EMITENTE
* (OK) campo 'obs' em dados do local de trabalho
* (OK) CORREÇÃO DO CALCULO NA TELA DE EDIÇÃO DE EMPRÉSTIMO(RETIREI O ONBLUR PQ NÃO PEGAVA O MÊS)
* (OK) CORRIGIR VALOR TOTAL DEVIDO NO CONTRATO
* (OK) NATURALIDADE NO CADASTRO DE FIADOR CNPJ
* (OK) DATA DE NASCIMENTO NO CADASTRO DE FIADOR CNPJ
* (OK) NUMERO CASA EM DADOS DE LOCAL DE TRABALHO
* (  ) SUBSTIRUIR O ENTER POR TAB
* (OK) TAB DE CLIENTE_CNPJ FIXADO
* (  ) TORNAR TUDO MAIUSCULO NO BANCO AO CRIAR O CLIENTE
* (OK) IDENTIFICAR O CLIENTE EM DESTAQUE NOS DETALHES DE EMPRÉSTIMO
* (  ) INSERIR OPÇÃO DE IMPRESSÃO DE CADASTRO DE CLIENTES (CPF E CNPJ)
* (  ) PADRONIZAR CAMPOS DE ENDEREÇO (CPF E CNPJ)
* (  ) C.E.T. AO MÊS 
* (  ) SUBIR O NOME DA CONTRACAPA  (??????????) NÃO ENTENDI ONDE DEVE FICAR O NOME
* (OK) tamanho do carne e espaços em branco sem espaços para descontos
* (  ) NACIONALIDADE BRASILEIRA POR PADRÃO E EDITÁVEL SE PRECISAR MUDAR
* (  ) mascara do RG
* (  ) GERADOR DE RECIBO DE PAGAMENTO DE EMPRÉSTIMO (A PRINCIPIO PARA CREDCOOP)
* (  ) CONTATOS É OBRIGATÓRIO APENAS UM CELULAR
* (  ) CAMPO DE NÚMERO CASA EM DADOS DE LOCAL DE TRABALHO
* (  ) MANTER TABS FIXAS EM TELAS DE CADASTRO
* (  ) CORRIGIR ESPAÇO GRANDE NO CONTRATO APÓS O QUADRO DE PARCELAS
* (  ) SE CASADO ABRIR CAMPO DE CONJUGE(NOME, CPF, TELEFONE)
* (  ) ABRIR AS IMPRESSÕES EM NOVA GUIA
* (  ) SE NÃO HOUVER REPRESENTANTE REPETIR OS DADOS DO CNPJ NA ABA REPRESENTANTE ???????
* (  ) 
* (  ) Cliente CNPJ terá boleto ao invés de carnê
* (  ) Preencher o campo nome fantasia automaticamente
* (  ) forma constituição opcional
* (  ) inscrição estadual tem mascara
* (  ) representante não ser obrigatório
* (  )

<!-- SUGESTÕES -->
* (  ) INSERIR HORA NO CABEÇALHO
* (  ) NÃO ESQUECER DE CORRIGIR A TAB DE CADASTRO EM MODO MOBILE
* (  )
* (  )
* (  )


