# Generated by Django 3.1 on 2020-09-22 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionacademica', '0008_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='nom_programa',
            field=models.CharField(default='', max_length=30),
        ),
    ]