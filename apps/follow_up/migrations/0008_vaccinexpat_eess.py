# Generated by Django 4.2.13 on 2024-09-19 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow_up', '0007_alter_vaccinexpat_descripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccinexpat',
            name='eess',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
