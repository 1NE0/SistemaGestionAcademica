# Generated by Django 3.1.4 on 2020-12-30 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionacademica', '0009_usuario_nom_programa'),
    ]

    operations = [
        migrations.CreateModel(
            name='periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_inicio', models.DateField()),
                ('Fecha_final', models.DateField()),
                ('Fecha_inscripcion', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='nivel_cursos',
            name='descripcion',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='detalle_curso',
            fields=[
                ('grupo', models.IntegerField(primary_key=True, serialize=False)),
                ('horario_inicial', models.DateField(verbose_name='')),
                ('horario_final', models.DateField(verbose_name='')),
                ('Nivel_Curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionacademica.nivel_cursos')),
            ],
        ),
        migrations.AddField(
            model_name='inscripciones',
            name='periodo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='gestionacademica.periodo'),
        ),
    ]
