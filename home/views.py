from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Recipe, Step, Ingredient, Favorite


# Create your views here.
def home_view(request):
    """
      View for home page.
    """
    return render(request, "home.html", {})


def favorite_view(request):
    user = request.user
    if request.method == 'POST':
        recipe_id = request.POST.get(
            'post_id')  # needs to be implemented in the main html (post_id needs to be defined)
        recipe_object = Recipe.objects.get(id=recipe_id)
        if user in recipe_object.like.all():
            recipe_object.like.remove(user)

        else:
            recipe_object.like.add(user)

        like_it, create = Favorite.objects.get_or_create(user=user, post_id=recipe_id)
        if not create:
            if like_it.value == "Like":
                like_it.value == "Unlike"
            else:
                like_it.value == "Like"

        like_it.save()

    return redirect("home:recipeView")

def add_ingredient(request,recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if(request.method == "POST"):
        ingredient_name = request.POST.get('ingredient')
        unit_name = request.POST.get('units')
        ingred = Ingredient.objects.create()
        unit_amount = request.POST.get('amount')
        ingred.name = ingredient_name
        ingred.units = unit_name
        ingred.quantity = unit_amount
        ingred.recipe.set(Recipe.objects.filter(id=recipe_id))
        recipe.save()
        ingred.save()
        return render(request, "recipe.html", context={"recipe":recipe,})
    else:
        return render(request, "ingredientSubmission.html", {})

def add_step(request,recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if(request.method == "POST"):
        step_text = request.POST.get('text')
        step = Step.objects.create()
        step.text = step_text
        step.recipe.set(Recipe.objects.filter(id=recipe_id))
        recipe.save()
        step.save()
        return render(request, "recipe.html", context={"recipe":recipe,})
    else:
        return render(request, "stepSubmission.html", {})

def submit_recipe(request):
    if (request.method == "POST"):
        recipe_title = request.POST.get('title')
        step_text = request.POST.get('text')
        ingredient_name = request.POST.get('ingredient')
        unit_name = request.POST.get('units')
        unit_amount = request.POST.get('amount')
        newRecipe = Recipe.objects.create()
        recid = newRecipe.id

        newRecipe.recipeTitle = recipe_title
        step = Step.objects.create()
        ingred = Ingredient.objects.create()
        step.text = step_text
        ingred.name = ingredient_name
        ingred.units = unit_name
        ingred.quantity = unit_amount
        step.recipe.set(Recipe.objects.filter(id=recid))
        ingred.recipe.set(Recipe.objects.filter(id=recid))
        newRecipe.save()
        ingred.save()
        step.save()
        return render(request, "recipe.html", context={"recipe":newRecipe,})
    else:
        return render(request, "recipeSubmission.html", {})


def template_testing_view_recipe(request):
    """
    A view to allow templates to be created before the backend is ready
    Should be removed for final release
    Written by Ben
    """
    return render(request, "add_recipe.html", {})

def template_testing_view_feed(request):
    """
    A view to allow templates to be created before the backend is ready
    Should be removed for final release
    Written by Ben
    """
    return render(request, "feed.html", {})


def recipeView(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    try:
        steps_select = recipe.step_set.all()
        ingredient_select = recipe.step_set.all()
        meal_type_select = recipe.meal_type_set.all()
        cuisine_type_select = recipe.cuisine_type_set.all()
    except(KeyError, recipe.DoesNotExist):
        return render(request, "home.html", {})
    else:
        return render(request, "recipe.html", context={"recipe":recipe,})
    """
    A view to allow templates to be created before the backend is ready
    Should be removed for final release
    Written by Ben
    """
