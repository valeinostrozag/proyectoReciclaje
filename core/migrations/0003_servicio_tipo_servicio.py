# Generated by Django 2.1.1 on 2019-11-20 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191119_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='tipo_servicio',
            field=models.CharField(choices=[('Fundacion', 'Fundacion'), ('Empresa', 'Empresa'), ('Casa particular', 'Casa particular'), ('Centro educacional', 'Centro educacional')], default='fhfhh', max_length=100),
            preserve_default=False,
        ),
    ]
