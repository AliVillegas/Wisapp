# Generated by Django 2.1.2 on 2018-11-06 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_userwithprofile_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userwithprofile',
            name='created_at',
        ),
    ]
