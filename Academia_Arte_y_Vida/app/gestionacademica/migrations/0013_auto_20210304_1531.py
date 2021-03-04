# Generated by Django 2.2.12 on 2021-03-04 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionacademica', '0012_detalle_curso_periodo'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscripcioncurso',
            name='periodo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='gestionacademica.periodo'),
        ),
        migrations.AddField(
            model_name='nivel_cursos',
            name='periodo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='gestionacademica.periodo'),
        ),
    ]
