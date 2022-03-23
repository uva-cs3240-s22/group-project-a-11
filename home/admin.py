from django.contrib import admin

# Register your models here.
from .models import Recipe, Ingredient, Step

admin.site.register([Recipe, Ingredient, Step])