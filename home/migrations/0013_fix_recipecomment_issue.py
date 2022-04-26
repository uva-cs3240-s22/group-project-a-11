from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_recipecomment_date_recipecomment_writer')
    ]

    operations = [
        migrations.AddField(
            model_name='recipecomment',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='date posted'),
        ),
    ]