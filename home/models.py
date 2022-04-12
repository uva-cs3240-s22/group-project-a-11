from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    published = models.BooleanField(default=False)
    recipeTitle = models.CharField(max_length=200)
    recipeText = models.TextField()
    image = models.FileField(upload_to='recipeImages', null=True)
    likes = models.ManyToManyField(User, related_name="likes")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="writer")

    def total_likes(self):
        return self.likes.count()

    time_to_make = models.IntegerField(default=60)

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
    image = models.FileField(upload_to='stepImages')
    # ^^ currently breaks addStep, will fix soon
    recipe = models.ManyToManyField(Recipe)

    def __str__(self):
        return str(self.text)

class Tag(models.Model):
    tag = models.CharField(max_length=500, default="")
    recipe = models.ManyToManyField(Recipe)
    def __str__(self):
        return str(self.tag)
