# Generated by Django 4.2.13 on 2024-07-09 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coverage',
            old_name='apo1_ref',
            new_name='dpta',
        ),
        migrations.RenameField(
            model_name='coverage',
            old_name='dpt1_ref',
            new_name='hav',
        ),
        migrations.RenameField(
            model_name='coverage',
            old_name='infl2_kids',
            new_name='infl2',
        ),
        migrations.RemoveField(
            model_name='coverage',
            name='infl3_kids',
        ),
        migrations.RemoveField(
            model_name='coverage',
            name='infl4_kids',
        ),
        migrations.RemoveField(
            model_name='coverage',
            name='neumo2',
        ),
        migrations.RemoveField(
            model_name='coverage',
            name='sector',
        ),
        migrations.RemoveField(
            model_name='coverage',
            name='tdap_preg',
        ),
        migrations.AddField(
            model_name='coverage',
            name='cod_eess',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
