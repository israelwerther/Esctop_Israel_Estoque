# Generated by Django 3.0.7 on 2020-08-18 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avalista', '0006_auto_20200818_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='avalista',
            name='fiador_copia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='avalista.Avalista'),
        ),
    ]
