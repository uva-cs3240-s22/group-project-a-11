# Generated by Django 4.0.2 on 2022-03-23 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0014_remove_recipe_writer_recipe_writer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='writer',
        ),
        migrations.AddField(
            model_name='recipe',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]