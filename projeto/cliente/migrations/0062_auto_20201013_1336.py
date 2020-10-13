# Generated by Django 3.0.7 on 2020-10-13 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0061_auto_20200930_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='conjuge_cpf',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='CPF'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='conjuge_nome',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='conjuge_telefone',
            field=models.CharField(blank=True, max_length=17, null=True, verbose_name='Celular '),
        ),
    ]
