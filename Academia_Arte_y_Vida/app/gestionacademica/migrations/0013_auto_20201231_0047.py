# Generated by Django 3.1.4 on 2020-12-31 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionacademica', '0012_auto_20201231_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiantes',
            name='ciudad',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionacademica.ciudad'),
        ),
    ]
