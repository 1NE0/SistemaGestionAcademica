# Generated by Django 2.2.12 on 2021-03-23 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionacademica', '0010_auto_20210320_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asignaturas',
            name='Docente',
        ),
        migrations.AddField(
            model_name='nivel_asignatura',
            name='docente',
            field=models.ForeignKey(default=999, on_delete=django.db.models.deletion.CASCADE, to='gestionacademica.Docentes'),
            preserve_default=False,
        ),
    ]
