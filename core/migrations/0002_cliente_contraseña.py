# Generated by Django 2.2.6 on 2019-11-13 20:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='contraseña',
            field=models.CharField(default=django.utils.timezone.now, max_length=80),
            preserve_default=False,
        ),
    ]
