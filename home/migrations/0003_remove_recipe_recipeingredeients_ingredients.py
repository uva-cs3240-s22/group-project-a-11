# Generated by Django 4.0.2 on 2022-03-22 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_recipe_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='recipeIngredeients',
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('units', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.recipe')),
            ],
        ),
    ]