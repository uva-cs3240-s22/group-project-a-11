# Generated by Django 4.0.2 on 2022-03-23 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_rename_ease_of_prep_recipe_difficulty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='cuisine_type',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='meal_type',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='steps',
        ),
        migrations.AddField(
            model_name='cuisine_type',
            name='recipe',
            field=models.ManyToManyField(to='home.Recipe'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ManyToManyField(to='home.Recipe'),
        ),
        migrations.AddField(
            model_name='meal_type',
            name='recipe',
            field=models.ManyToManyField(to='home.Recipe'),
        ),
        migrations.AddField(
            model_name='step',
            name='recipe',
            field=models.ManyToManyField(to='home.Recipe'),
        ),
    ]
