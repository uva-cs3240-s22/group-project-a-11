from django.contrib import admin

# Register your models here.
from .models import Recipe, Favorited

admin.site.register(Recipe)