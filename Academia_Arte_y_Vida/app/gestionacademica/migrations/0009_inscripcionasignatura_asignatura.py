# Generated by Django 2.2.12 on 2021-03-20 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionacademica', '0008_auto_20210320_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscripcionasignatura',
            name='asignatura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionacademica.Asignaturas'),
        ),
    ]
