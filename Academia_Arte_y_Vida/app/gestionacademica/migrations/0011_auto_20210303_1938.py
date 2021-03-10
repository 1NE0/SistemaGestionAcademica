# Generated by Django 2.2.12 on 2021-03-03 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionacademica', '0010_remove_docentes_pagorealizado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalle_curso',
            name='cod_estudiante',
        ),
        migrations.RemoveField(
            model_name='detalle_curso',
            name='horario_final',
        ),
        migrations.RemoveField(
            model_name='detalle_curso',
            name='horario_inicial',
        ),
        migrations.RemoveField(
            model_name='nivel_asignatura',
            name='horario_final',
        ),
        migrations.RemoveField(
            model_name='nivel_asignatura',
            name='horario_inicial',
        ),
        migrations.AddField(
            model_name='detalle_curso',
            name='dia',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='detalle_curso',
            name='horaFinal',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='detalle_curso',
            name='horaInicio',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='nivel_asignatura',
            name='dia',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='nivel_asignatura',
            name='horaFinal',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='nivel_asignatura',
            name='horaInicio',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='programas',
            name='duracion',
            field=models.IntegerField(default=9999),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='inscripcionEstudianteCurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle_curso', models.ForeignKey(default='nulo', on_delete=django.db.models.deletion.CASCADE, to='gestionacademica.detalle_curso')),
                ('estudiante', models.ForeignKey(default='nulo', on_delete=django.db.models.deletion.CASCADE, to='gestionacademica.Estudiantes')),
            ],
        ),
    ]