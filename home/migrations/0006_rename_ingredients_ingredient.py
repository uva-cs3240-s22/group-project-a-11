# Generated by Django 4.0.2 on 2022-03-23 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_steps_step'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingredients',
            new_name='Ingredient',
        ),
    ]
