from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipeTitle = models.CharField(max_length=200)
    recipeText = models.TextField()
    writer = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.recipeTitle

class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    units = models.CharField(max_length=200)
    quantity = models.IntegerField()
    def __str__(self):
        return self.name