# Generated by Django 2.2.6 on 2019-11-18 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20191118_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='descripcion_servicio',
            field=models.TextField(max_length=200),
        ),
    ]