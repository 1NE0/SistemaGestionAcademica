# Generated by Django 2.2.12 on 2021-02-03 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionacademica', '0002_auto_20210203_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodo',
            name='codigo',
            field=models.IntegerField(default='999', primary_key=True, serialize=False),
        ),
    ]
