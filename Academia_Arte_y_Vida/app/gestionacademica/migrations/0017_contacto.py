# Generated by Django 3.1.6 on 2021-04-08 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionacademica', '0016_auto_20210408_0040'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('mensaje', models.TextField(max_length=1000)),
            ],
        ),
    ]
