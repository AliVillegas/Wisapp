# Generated by Django 2.1.2 on 2018-11-03 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_auto_20181103_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Event', verbose_name='evento(si pertenece a un evento)'),
        ),
    ]