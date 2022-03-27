from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    recipeTitle = models.CharField(max_length=200)
    recipeText = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    likes = models.IntegerField(default=0)
    time_to_make = models.IntegerField(default=60)
    """steps = models.ManyToManyField(Step)
    ingredients = models.ManyToManyField(Ingredient)

    meal_type = models.ManyToManyField(Meal_Type)
    cuisine_type = models.ManyToManyField(Cuisine_Type)"""

    parentRecipe = models.ForeignKey('self', unique=False, related_name="childrenRecipe", on_delete=models.CASCADE,
                                     null=True, blank=True)

    BEGINNER = 'BE'
    INTERMEDIATE = 'IN'
    ADVANCED = 'AD'
    DIFFICULTY_CHOICES = [
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
    ]
    difficulty = models.CharField(
        max_length=2,
        choices=DIFFICULTY_CHOICES,
        default=INTERMEDIATE,
    )

    def __str__(self) -> str:
        return str(self.recipeTitle)


class Meal_Type(models.Model):
    name = models.CharField(max_length=200)
    recipe = models.ManyToManyField(Recipe)
    def __str__(self):
        return self.name
class Cuisine_Type(models.Model):
    name = models.CharField(max_length=200)
    recipe = models.ManyToManyField(Recipe)
    def __str__(self):
        return self.name
class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    units = models.CharField(max_length=200, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    qualifier = models.CharField(max_length=200, blank=True, null=True)
    recipe = models.ManyToManyField(Recipe)
    def __str__(self):
        return str(self.name)

class Step(models.Model):
    text = models.CharField(max_length=500, default="")
    asset_url = models.CharField(max_length=200, blank=True) # Will change when we figure out images
    recipe = models.ManyToManyField(Recipe)
    def __str__(self):
        return str(self.text)