# Generated by Django 3.1.6 on 2021-04-08 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionacademica', '0015_pqrs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pqrs',
            name='tipoSolicitante',
            field=models.CharField(choices=[('1', 'Estudiante'), ('2', 'Colaborador'), ('3', 'Docente'), ('4', 'Egresado'), ('5', 'Externo'), ('6', 'Proveedor'), ('7', 'Otro')], default='', max_length=20),
        ),
    ]