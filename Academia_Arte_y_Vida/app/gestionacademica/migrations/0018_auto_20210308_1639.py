# Generated by Django 2.2.12 on 2021-03-08 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionacademica', '0017_auto_20210308_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nivel_cursos',
            name='Docente',
        ),
        migrations.RemoveField(
            model_name='nivel_cursos',
            name='periodo',
        ),
        migrations.AddField(
            model_name='detalle_curso',
            name='Docente',
            field=models.ForeignKey(default=999, on_delete=django.db.models.deletion.CASCADE, to='gestionacademica.Docentes'),
            preserve_default=False,
        ),
    ]