# Generated by Django 2.1.2 on 2018-11-12 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0053_petitionforadmin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petitionforadmin',
            name='message',
            field=models.CharField(max_length=1000, verbose_name='descripción de la petición'),
        ),
    ]