# Generated by Django 4.1.7 on 2023-05-29 21:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0014_alter_comment_user_alter_rating_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
