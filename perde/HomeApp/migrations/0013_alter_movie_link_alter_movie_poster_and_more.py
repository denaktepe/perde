# Generated by Django 4.1.7 on 2023-04-10 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0012_remove_movie_genre_movie_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='link',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='movie',
            name='trailer',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
