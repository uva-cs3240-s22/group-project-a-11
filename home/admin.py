from django.contrib import admin

# Register your models here.
from .models import Recipe, Favorite

admin.site.register(Recipe)
admin.site.register(Favorite)