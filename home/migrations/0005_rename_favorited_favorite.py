# Generated by Django 4.0.2 on 2022-03-26 18:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_remove_recipe_likes_recipe_like_favorited'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Favorited',
            new_name='Favorite',
        ),
    ]
