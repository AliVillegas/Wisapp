# Generated by Django 2.1.2 on 2018-11-06 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_auto_20181104_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='userwithprofile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de Creación'),
        ),
    ]