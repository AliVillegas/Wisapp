# Generated by Django 2.1.2 on 2018-11-02 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20181101_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='event',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Event'),
        ),
    ]