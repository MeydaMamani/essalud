# Generated by Django 4.2.13 on 2024-08-23 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow_up', '0004_alter_anemia_edad_mes'),
    ]

    operations = [
        migrations.AddField(
            model_name='anemia',
            name='enf10',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='anemia',
            name='enf11',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='anemia',
            name='enf6',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='anemia',
            name='enf7',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='anemia',
            name='enf8',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='anemia',
            name='enf9',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='anemia',
            name='grupo_edad',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]