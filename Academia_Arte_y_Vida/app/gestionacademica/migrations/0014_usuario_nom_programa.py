# Generated by Django 3.1.4 on 2020-12-31 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionacademica', '0013_auto_20201231_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='nom_programa',
            field=models.CharField(default='', max_length=60),
        ),
    ]