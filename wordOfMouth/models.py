from django.db import models
from django import forms
from django.utils import timezone

#Models here
class Recipe(models.Model):
    recipeTitle = models.CharField(max_length=200)
    recipeText = models.TextField()
    recipeIngredeients = models.CharField()
    writer = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.recipeTitle
