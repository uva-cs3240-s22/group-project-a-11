# Generated by Django 4.0.2 on 2022-04-17 17:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0010_remove_recipe_like_recipe_likes_alter_tag_recipe_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='RecipeComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=500)),
                ('recipe', models.ManyToManyField(to='home.Recipe')),
            ],
        ),
    ]