# Generated by Django 2.1.2 on 2018-11-05 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_category_isevent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categoría o Evento', 'verbose_name_plural': 'Categorías o Eventos'},
        ),
        migrations.RemoveField(
            model_name='story',
            name='event',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]