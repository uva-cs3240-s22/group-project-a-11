# Generated by Django 4.0.2 on 2022-03-23 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_remove_recipe_writer_recipe_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ease_of_prep',
            field=models.CharField(choices=[('BE', 'Beginner'), ('IN', 'Intermediate'), ('AD', 'Advanced')], default='IN', max_length=2),
        ),
    ]