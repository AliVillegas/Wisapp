# Generated by Django 2.1.2 on 2018-11-03 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_auto_20181103_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='event',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.Event', verbose_name='evento(si pertenece a un evento)'),
        ),
    ]