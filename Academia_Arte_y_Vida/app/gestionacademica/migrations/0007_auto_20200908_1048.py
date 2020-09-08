# Generated by Django 3.0.7 on 2020-09-08 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionacademica', '0006_auto_20200907_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='dia',
            field=models.CharField(choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miercoles', 'Miercoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sabado', 'Sabado')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='h_final',
            field=models.CharField(choices=[('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00')], default='10:00', max_length=5),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='h_inicio',
            field=models.CharField(choices=[('8:00', '8:00'), ('9:00', '9:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00')], default='8:00', max_length=5),
        ),
    ]