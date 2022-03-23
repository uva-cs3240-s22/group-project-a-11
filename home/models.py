from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meal_Type(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Cuisine_Type(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    units = models.CharField(max_length=200, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    qualifier = models.CharField(max_length=200, blank=True, null=True)
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
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    likes = models.IntegerField(default=0)
    time_to_make = models.IntegerField(default=60)
    steps = models.ManyToManyField(Step)
    ingredients = models.ManyToManyField(Ingredient)

    meal_type = models.ManyToManyField(Meal_Type)
    cuisine_type = models.ManyToManyField(Cuisine_Type)

    parentRecipe = models.ForeignKey('self', unique=False, related_name="childrenRecipe", on_delete=models.CASCADE, null=True, blank=True)

    
    def __str__(self) -> str:
        return self.recipeTitle