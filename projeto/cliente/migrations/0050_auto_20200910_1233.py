# Generated by Django 3.0.7 on 2020-09-10 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0049_cliente_tipo_de_conta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='anotacoes',
        ),
        migrations.AddField(
            model_name='cliente',
            name='n_operacao',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Nº operação'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='agencia',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Nº agência'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='conta',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Nº conta'),
        ),
    ]
