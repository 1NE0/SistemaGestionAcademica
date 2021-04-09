# Generated by Django 3.1.6 on 2021-04-07 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionacademica', '0014_inscripcioncurso_periodo'),
    ]

    operations = [
        migrations.CreateModel(
            name='pqrs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCompleto', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('tipoSolicitante', models.CharField(choices=[('Est', 'Estudiante'), ('Col', 'Colaborador'), ('doc', 'Docente'), ('Egr', 'Egresado'), ('Ext', 'Externo'), ('Prov', 'Proveedor'), ('otro', 'Otro')], default='', max_length=20)),
                ('celular', models.CharField(max_length=10)),
                ('tipoSolicitud', models.CharField(choices=[('1', 'Felicitaciones'), ('2', 'Sugerencias'), ('3', 'Peticiones'), ('4', 'Quejas'), ('5', 'Reclamos'), ('6', 'Comentarios'), ('7', 'Otro')], default='', max_length=20)),
                ('solicitudServicio', models.CharField(choices=[('1', 'Académicos'), ('2', 'Administrativos'), ('3', 'Consultor'), ('4', 'Tecnología'), ('5', 'Otro')], default='', max_length=20)),
                ('comentario', models.TextField(max_length=1000)),
                ('ciudad', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='gestionacademica.ciudad')),
            ],
        ),
    ]
