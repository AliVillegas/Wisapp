# Generated by Django 2.1.2 on 2018-11-06 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0044_userwithprofile_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userwithprofile',
            name='created_at',
        ),
        migrations.AddField(
            model_name='story',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de Creación'),
        ),
    ]