# Generated by Django 2.2.12 on 2021-03-20 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionacademica', '0006_auto_20210320_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscripcionasignatura',
            name='nivel_asignatura',
        ),
        migrations.AddField(
            model_name='nivel_asignatura',
            name='inscripcion_asignatura',
            field=models.ForeignKey(default=999, on_delete=django.db.models.deletion.CASCADE, to='gestionacademica.InscripcionAsignatura'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='InscripcionEstudianteAsignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_realizacion', models.DateField(default='')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionacademica.Estudiantes')),
                ('inscripcion_estudiante', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionacademica.InscripcionEstudiante')),
                ('nivel_asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionacademica.Nivel_asignatura')),
            ],
        ),
    ]