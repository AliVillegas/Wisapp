# Generated by Django 2.1.2 on 2018-11-03 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20181102_1807'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categoría', 'verbose_name_plural': 'Categorías'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Comentario', 'verbose_name_plural': 'Comentarios'},
        ),
        migrations.AlterModelOptions(
            name='story',
            options={'verbose_name': 'Historia', 'verbose_name_plural': 'Historias'},
        ),
        migrations.AlterModelOptions(
            name='userwithprofile',
            options={'verbose_name': 'Usuario(Perfil)', 'verbose_name_plural': 'Usuarios(Perfil)'},
        ),
    ]