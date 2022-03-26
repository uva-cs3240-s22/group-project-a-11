from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    recipeTitle = models.CharField(max_length=200)
    recipeText = models.TextField()
    writer = models.CharField(max_length=200)
    # likes = models.IntegerField(default=0)
    like = models.ManyToManyField(User, default=None, blank=True)
    def __str__(self) -> str:
        return self.recipeTitle

    @property
    def number_of_likes(self):
        return self.like.all().count()


class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    units = models.CharField(max_length=200)
    quantity = models.IntegerField()
    def __str__(self):
        return self.name

class Favorited(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_liked = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    like_option = models.CharField(default='Like', max_length=10)

    def __str__(self):
        return str(self.recipe_liked)