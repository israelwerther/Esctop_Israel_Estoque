# Generated by Django 3.0.7 on 2020-09-11 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0056_auto_20200911_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='referencia_trabalho',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Ponto de Referencia'),
        ),
    ]
