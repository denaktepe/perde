# Generated by Django 4.1.7 on 2023-04-09 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0004_actor_birth_day_actor_country_director_birth_day_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='movies',
            field=models.ManyToManyField(related_name='genres', to='HomeApp.movie'),
        ),
    ]