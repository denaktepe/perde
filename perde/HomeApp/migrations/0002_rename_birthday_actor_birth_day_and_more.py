# Generated by Django 4.1.7 on 2023-04-09 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='birthDay',
            new_name='birth_day',
        ),
        migrations.RenameField(
            model_name='director',
            old_name='birthDay',
            new_name='birth_day',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='movies',
            new_name='favorite_movies',
        ),
    ]