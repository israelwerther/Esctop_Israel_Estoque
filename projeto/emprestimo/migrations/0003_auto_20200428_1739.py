# Generated by Django 3.0.5 on 2020-04-28 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0002_auto_20200428_1647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emprestimoitens',
            old_name='estoque',
            new_name='emprestimo',
        ),
    ]
