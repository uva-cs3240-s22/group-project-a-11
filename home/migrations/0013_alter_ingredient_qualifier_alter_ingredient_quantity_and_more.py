# Generated by Django 4.0.2 on 2022-03-23 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_recipe_parentrecipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='qualifier',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='units',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
