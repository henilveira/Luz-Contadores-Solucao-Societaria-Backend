# Generated by Django 5.1.1 on 2024-10-16 03:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidades', '0003_rename_abertura_contabilidade_data_abertura'),
        ('societario', '0002_remove_aberturaempresa_atividade_principal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aberturaempresa',
            name='contabilidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contabilidades.contabilidade'),
        ),
    ]
