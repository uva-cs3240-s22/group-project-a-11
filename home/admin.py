from django.contrib import admin

# Register your models here.
from .models import Recipe, Ingredient, Step, Meal_Type, Cuisine_Type

admin.site.register([Recipe, Ingredient, Step, Meal_Type, Cuisine_Type])
