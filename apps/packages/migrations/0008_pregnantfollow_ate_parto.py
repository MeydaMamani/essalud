# Generated by Django 4.2.13 on 2024-09-06 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0007_pregnantfollow_aro_pregnantfollow_bro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregnantfollow',
            name='ate_parto',
            field=models.DateField(blank=True, null=True),
        ),
    ]