# Generated by Django 2.2.12 on 2021-04-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionacademica', '0017_contacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='referenciaPago',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
