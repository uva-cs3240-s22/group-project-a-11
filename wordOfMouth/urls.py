"""wordOfMouth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import submit_recipe
from home.views import home_view, recipeView, add_step, \
    add_ingredient, delete_ingredient, likeView, delete_step, feed_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'wordOfMouth'
urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('', home_view, name='home'),
    path('recipeSubmission', submit_recipe, name='recipeSubmission'),
    path('recipe/<int:recipe_id>', recipeView, name="recipe"),
    path('ingredAdd/<int:recipe_id>', add_ingredient, name="ingredient-adding"),
    path('stepAdd/<int:recipe_id>', add_step, name="step-adding"),
    path('deleteI/<int:recipe_id>/<int:ingredient_id>', delete_ingredient, name="delete-ingredient"),
    path('deleteS/<int:recipe_id>/<int:step_id>', delete_step, name="delete-step"),
    path('like/<int:pk>', likeView, name='like'),
    path('feed', feed_view, name="feed")
]

urlpatterns += staticfiles_urlpatterns()
