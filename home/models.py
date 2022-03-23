from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    units = models.CharField(max_length=200, blank=True)
    quantity = models.IntegerField(blank=True)
    qualifier = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.name

class Step(models.Model):
    text = models.CharField(max_length=500, default="")
    asset_url = models.CharField(max_length=200, blank=True) # Will change when we figure out images
    def __str__(self):
        return self.text

class Recipe(models.Model):
    recipeTitle = models.CharField(max_length=200)
    recipeText = models.TextField()
    writer = models.OneToOneField(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    time_to_make = models.IntegerField(default=60)
    steps = models.ManyToManyField(Step)
    ingredients = models.ManyToManyField(Ingredient)
    def __str__(self) -> str:
        return self.recipeTitle