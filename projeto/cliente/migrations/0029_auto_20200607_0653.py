# Generated by Django 3.0.6 on 2020-06-07 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0028_remove_cliente_ibge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('solteiro', 'Solteiro'), ('casado', 'Casado')], max_length=15, null=True, verbose_name='Estado Civil'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='naturalidade',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='naturalidade'),
        ),
    ]
