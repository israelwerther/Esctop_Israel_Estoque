# Generated by Django 3.0.6 on 2020-05-21 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0016_auto_20200521_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='naturalidade',
            field=models.DateField(blank=True, max_length=15, null=True, verbose_name='Naturalidade'),
        ),
    ]
