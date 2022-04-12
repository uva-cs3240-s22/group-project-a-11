# Generated by Django 4.0.2 on 2022-04-11 12:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0009_step_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='like',
        ),
        migrations.AddField(
            model_name='recipe',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tag',
            name='recipe',
            field=models.ManyToManyField(to='home.Recipe'),
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]
