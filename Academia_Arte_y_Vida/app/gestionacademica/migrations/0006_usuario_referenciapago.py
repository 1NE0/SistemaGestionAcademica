# Generated by Django 2.2.12 on 2021-02-04 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionacademica', '0005_remove_asignaturas_cod_inscripcionprograma'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='referenciaPago',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]