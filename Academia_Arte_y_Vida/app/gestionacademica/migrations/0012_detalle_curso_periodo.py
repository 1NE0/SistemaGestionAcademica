# Generated by Django 2.2.12 on 2021-03-03 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionacademica', '0011_auto_20210303_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle_curso',
            name='periodo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='gestionacademica.periodo'),
        ),
    ]