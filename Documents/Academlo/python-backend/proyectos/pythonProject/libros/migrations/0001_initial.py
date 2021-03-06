# Generated by Django 2.2.24 on 2021-10-27 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autores', '0002_auto_20211027_0149'),
        ('editoriales', '0002_auto_20211027_0149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('paginas', models.IntegerField()),
                ('publicado', models.BooleanField()),
                ('fecha_publicacion', models.DateField()),
                ('autores', models.ManyToManyField(related_name='libros', to='autores.Autor')),
                ('editorial', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='libros', to='editoriales.Editorial')),
            ],
        ),
    ]
