# Generated by Django 3.0.7 on 2021-01-24 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionacademica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programas',
            name='periodo',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionacademica.periodo'),
        ),
    ]
