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
from home.views import add_comment, home_view
from home.views import submit_recipe
from home.views import home_view, template_testing_view_recipe, recipeView, template_testing_view_feed, add_step, add_ingredient, favorite_view

app_name = 'wordOfMouth'
urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('', home_view, name='home'),
    path('recipeSubmission', submit_recipe, name='recipeSubmission'),
    path('like/', favorite_view, name="favorite-view"),
    path('recipe-template-testing/', template_testing_view_recipe, name="recipe_template-testing"),
    path('recipe/<int:recipe_id>' , recipeView, name="recipe_add_template-testing"),
    path('feed-template-testing/', template_testing_view_feed, name="feed_template-testing"),
    path('ingredAdd/<int:recipe_id>', add_ingredient, name="ingredient-adding"),
    path('stepAdd/<int:recipe_id>', add_step, name="step-adding"),
    path('commentAdd/<int:recipe_id>', add_comment, name="comment-adding"),

]
