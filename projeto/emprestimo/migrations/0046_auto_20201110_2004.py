# Generated by Django 3.0.7 on 2020-11-10 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0045_auto_20201110_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='juros_ao_mes',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Juros ao mês'),
        ),
    ]
