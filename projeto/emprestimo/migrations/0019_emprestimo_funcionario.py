# Generated by Django 3.0.6 on 2020-06-11 05:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emprestimo', '0018_remove_emprestimo_funcionario'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimo',
            name='funcionario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
