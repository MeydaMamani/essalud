# Generated by Django 4.2.13 on 2024-08-23 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0004_pregnantfollow_den_pregnantfollow_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregnantfollow',
            name='c10_c11',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pregnantfollow',
            name='c1_c2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pregnantfollow',
            name='c2_c3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pregnantfollow',
            name='c3_c4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pregnantfollow',
            name='c4_c5',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pregnantfollow',
            name='c5_c6',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pregnantfollow',
            name='c6_c7',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pregnantfollow',
            name='c7_c8',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pregnantfollow',
            name='c8_c9',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pregnantfollow',
            name='c9_c10',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pregnantfollow',
            name='dx_anemia',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pregnantfollow',
            name='edad_cap',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pregnantfollow',
            name='fpp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='pregnantfollow',
            name='fur',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pregnantfollow',
            name='ini_sem28',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pregnantfollow',
            name='ini_sem33',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pregnantfollow',
            name='laboratorio',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pregnantfollow',
            name='max_sem13',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pregnantfollow',
            name='peso',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='pregnantfollow',
            name='result',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pregnantfollow',
            name='sem_captada',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='pregnantfollow',
            name='suple_ant13',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pregnantfollow',
            name='talla',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
