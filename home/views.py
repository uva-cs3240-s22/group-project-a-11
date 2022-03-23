from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Recipe


# Create your views here.
def home_view(request):
    """
      View for home page.
    """
    return render(request, "home.html", {})


def submit_recipe(request):
    if(request.method == "POST"):
        recipe_title = request.POST['title']
        recipe_text = request.POST['text']
        newRecipe = Recipe.objects.create();
        newRecipe.recipeTitle = recipe_title
        newRecipe.recipeText = recipe_text
        newRecipe.save()
        return HttpResponseRedirect('/recipe/')
    else:
        return render(request, 'recipeSubmission.html')

class RecipeView(generic.ListView):
    model = Recipe
    template_name = 'recipeView.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Recipe.objects.all()


def template_testing_view_recipe(request):
    """
    A view to allow templates to be created before the backend is ready
    Should be removed for final release
    Written by Ben
    """
    return render(request, "recipe.html", {})


def template_testing_view_feed(request):
    """
    A view to allow templates to be created before the backend is ready
    Should be removed for final release
    Written by Ben
    """
    return render(request, "feed.html", {})


def template_testing_view_recipe_add(request):
    """
    A view to allow templates to be created before the backend is ready
    Should be removed for final release
    Written by Ben
    """
    return render(request, "recipe_add.html", {})
