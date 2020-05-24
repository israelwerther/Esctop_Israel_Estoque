# Generated by Django 3.0.6 on 2020-05-24 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0016_auto_20200522_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='bairro_trabalho',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Bairro'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='celular1_trabalho',
            field=models.CharField(blank=True, max_length=17, null=True, verbose_name='celular 1'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='celular2_trabalho',
            field=models.CharField(blank=True, max_length=17, null=True, verbose_name='celular 2'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='cep_trabalho',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='CEP'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='cidade_trabalho',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Cidade'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='contato1_trabalho',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Contato 1'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='contato2_trabalho',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Contato 2'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='ibge_trabalho',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='IBGE'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='nome_fantasia',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome Fantasia'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='numero_casa_trabalho',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Nº '),
        ),
        migrations.AddField(
            model_name='cliente',
            name='rua_trabalho',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Rua'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='uf_trabalho',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='Estado'),
        ),
    ]
