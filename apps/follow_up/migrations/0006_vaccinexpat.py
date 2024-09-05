# Generated by Django 4.2.13 on 2024-09-05 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow_up', '0005_anemia_enf10_anemia_enf11_anemia_enf6_anemia_enf7_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VaccinexPat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(blank=True, null=True)),
                ('mes', models.IntegerField(blank=True, null=True)),
                ('fec_atencion', models.DateField(blank=True, null=True)),
                ('id_eess', models.IntegerField(blank=True, null=True)),
                ('tipo_doc', models.CharField(blank=True, max_length=20, null=True)),
                ('documento', models.CharField(blank=True, max_length=15, null=True)),
                ('fec_nac', models.DateField(blank=True, null=True)),
                ('codigo', models.CharField(blank=True, max_length=15, null=True)),
                ('lab', models.CharField(blank=True, max_length=15, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=500, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('tipo_edad', models.CharField(blank=True, max_length=5, null=True)),
                ('anio_act', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]