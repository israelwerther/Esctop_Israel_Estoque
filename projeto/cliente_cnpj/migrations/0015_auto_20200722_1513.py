# Generated by Django 3.0.7 on 2020-07-22 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente_cnpj', '0014_auto_20200722_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente_cnpj',
            name='cnpj',
            field=models.CharField(blank=True, max_length=36, null=True, unique=True, verbose_name='CNPJ'),
        ),
    ]
