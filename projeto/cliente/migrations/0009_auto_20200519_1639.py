# Generated by Django 3.0.5 on 2020-05-19 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0008_auto_20200519_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='endereco',
        ),
        migrations.AddField(
            model_name='cliente',
            name='ponto_referencia',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ponto de Referencia'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='rua',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Rua'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='numero_casa',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Nº '),
        ),
    ]
