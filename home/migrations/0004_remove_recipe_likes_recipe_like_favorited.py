# Generated by Django 4.0.2 on 2022-03-26 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0003_remove_recipe_recipeingredeients_ingredients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='likes',
        ),
        migrations.AddField(
            model_name='recipe',
            name='like',
            field=models.ManyToManyField(blank=True, default=None, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Favorited',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_option', models.CharField(default='Like', max_length=10)),
                ('recipe_liked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),

        migrations.AddField(
            model_name='ingredients',
            name='qualifier',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='recipe',
            name='time_to_make',
            field=models.IntegerField(default=60),
        ),
        migrations.RemoveField(
            model_name='ingredients',
            name='recipe',
        ),
        migrations.AddField(
            model_name='ingredients',
            name='recipe',
            field=models.ManyToManyField(to='home.Recipe'),
        ),
        migrations.CreateModel(
            name='Steps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('units', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('qualifier', models.CharField(blank=True, max_length=200)),
                ('recipe', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.recipe')),
            ],
        ),
    ]
