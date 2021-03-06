# Generated by Django 2.2.24 on 2021-10-27 01:49

import calendar
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='apellido',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='autor',
            name='direccion',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='autor',
            name='email',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='autor',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='autor',
            name='fecha_nacimiento',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=calendar.Calendar),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='autor',
            name='telefono',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
