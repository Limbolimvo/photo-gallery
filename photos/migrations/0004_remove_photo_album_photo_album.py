# Generated by Django 4.1.7 on 2023-04-18 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_alter_album_options_alter_album_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='album',
        ),
        migrations.AddField(
            model_name='photo',
            name='album',
            field=models.ManyToManyField(null=True, to='photos.album'),
        ),
    ]
