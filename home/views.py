from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Recipe, Step, Ingredient, Tag


# Create your views here.
def home_view(request):
    """
      View for home page.
    """
    return render(request, "home.html", {})


def likeView(request, pk):
    recipe = get_object_or_404(Recipe, id=request.POST.get('button_id'))

    liked = False
    if recipe.likes.filter(id=request.user.id).exists():
        recipe.likes.remove(request.user)
        liked = False
    else:
        recipe.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('recipe', args=[str(pk)]))


def add_ingredient(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == "POST":
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
        return render(request, "recipe.html", context={"recipe": recipe})
    else:
        return render(request, "ingredientSubmission.html", {})


def add_step(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == "POST":
        step_text = request.POST.get('text')
        step = Step.objects.create(text=step_text)
        step.text = step_text
        step.recipe.set(Recipe.objects.filter(id=recipe_id))
        recipe.save()
        step.save()
        return render(request, "recipe.html", context={"recipe": recipe})
    else:
        return render(request, "stepSubmission.html", {})


def submit_recipe(request):
    if request.method == "POST":
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
        return render(request, "recipe.html", context={"recipe": newRecipe})
    else:
        return render(request, "recipeSubmission.html", {})


def delete_ingredient(request, ingredient_id, recipe_id):
    ingredient = get_object_or_404(Ingredient, pk=ingredient_id)
    ingredient.delete()
    return HttpResponseRedirect(reverse('recipe', args=recipe_id))


def delete_step(request, step_id, recipe_id):
    step = get_object_or_404(Step, pk=step_id)
    step.delete()
    return HttpResponseRedirect(reverse('recipe', args=(recipe_id,)))


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
    if 'tag_add' in request.POST:
        tag = Tag.objects.create()
        tag.tag = request.POST.get('tag_add')
        tag.recipe.set(Recipe.objects.filter(id=recipe_id))
        tag.save()
        recipe.save()
        return render(request, "recipe.html", context={"recipe":recipe,})
    try:
        steps_select = recipe.step_set.all()
        ingredient_select = recipe.step_set.all()
        meal_type_select = recipe.meal_type_set.all()
        cuisine_type_select = recipe.cuisine_type_set.all()
        total_likes = recipe.total_likes()
    except(KeyError, recipe.DoesNotExist):
        return render(request, "home.html", {})
    else:
        return render(request, "recipe.html", context={"recipe":recipe,})
