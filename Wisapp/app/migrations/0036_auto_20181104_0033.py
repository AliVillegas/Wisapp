# Generated by Django 2.1.2 on 2018-11-04 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_userwithprofile_followedcategories'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='image',
            field=models.FileField(blank=True, default='pic_folder/None/no-img.jpg', null=True, upload_to='pic_folder/'),
        ),
        migrations.AlterField(
            model_name='userwithprofile',
            name='writtenStories',
            field=models.ManyToManyField(blank=True, related_name='WrittenStories', to='app.Story', verbose_name='Historias escritas'),
        ),
    ]
