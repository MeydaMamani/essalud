# Generated by Django 4.2.13 on 2024-10-03 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow_up', '0009_inmunization'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inmunization',
            old_name='id_eess',
            new_name='cod_eess',
        ),
    ]
