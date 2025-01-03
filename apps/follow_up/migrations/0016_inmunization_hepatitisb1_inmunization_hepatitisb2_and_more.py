# Generated by Django 4.2.13 on 2024-12-07 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow_up', '0015_rename_apo1_ref_inmunization_gest_dt1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmunization',
            name='hepatitisb1',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inmunization',
            name='hepatitisb2',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inmunization',
            name='hepatitisb3',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inmunization',
            name='ref_dpt2',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inmunization',
            name='tdoc',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='inmunization_c',
            name='hepatitisb1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inmunization_c',
            name='hepatitisb2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inmunization_c',
            name='hepatitisb3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inmunization_c',
            name='ref_dpt2',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
