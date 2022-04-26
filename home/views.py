from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Recipe, Step, Ingredient, Tag, User, RecipeComment
from django.db.models import Count
from django.views.generic.list import ListView


# Create your views here.
def home_view(request):
    """
      View for home page.
    """
    return render(request, "home.html", {})


def likeView(request, pk):
    recipe = get_object_or_404(Recipe, id=request.POST.get('button_id'))

    if recipe.likes.filter(id=request.user.id).exists():
        recipe.likes.remove(request.user)
    else:
        recipe.likes.add(request.user)

    return HttpResponseRedirect(reverse('recipe', args=[str(pk)]))

def taggedRecipes(request, tag_id):
    tagCheck = get_object_or_404(Tag, id=tag_id)
    recipeTag = Recipe.objects.filter(tag__tag = tagCheck.tag)
    return render(request,'tagView.html', context={'recipes' : recipeTag, 'tag' : tagCheck})


# meet with Ben and decide on formatting for html file

#def user_liked_recipes(request):
    #the_user = request.user
    #my_liked_recipes = Recipe.likes.filter(id=the_user)
    #return render(request, 'my_liked_recipes.html', {'recipes': my_liked_recipes})


# def user_recipes(request):
#     the_user = request.user
#     my_recipes = Recipe.objects.filter(writer=the_user)
#     return render(request, 'my_recipes.html', {'recipes': my_recipes})

def recipe_feed_view(request):
    the_user = request.user
    sort_by = "id"
    if request.method == 'GET' and 'sort' in request.GET:
        sort_by = request.GET['sort']
    if request.method == 'GET' and 'r' in request.GET:
        sort_by = "-" + sort_by

    if sort_by == "likes":
        my_recipes = Recipe.objects.filter(writer=the_user).annotate(q_count=Count('likes')).order_by('-q_count')
    else:
        my_recipes = Recipe.objects.filter(writer=the_user).order_by(sort_by)
    return render(request, "my_recipes.html", context={"recipes": my_recipes, "sort": sort_by})


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
        return HttpResponseRedirect(reverse('recipe', args=[recipe_id]))
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
        return HttpResponseRedirect(reverse('recipe', args=[recipe_id]))
    else:
        return render(request, "stepSubmission.html", {})


def add_comment(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == "POST":
        comment_text = request.POST.get('text')
        comment = RecipeComment.objects.create()
        # print("Comment text: ")
        # print(comment_text)
        comment.text = comment_text
        comment.recipe.set(Recipe.objects.filter(id=recipe_id))
        comment.writer = request.user
        recipe.save()
        comment.save()
        return HttpResponseRedirect(reverse('recipe', args=[recipe_id]))
    else:
        return render(request, "commentSubmission.html", {})


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
        newRecipe.time_to_make = request.POST.get('time_to_make')
        newRecipe.image = request.FILES.get('img_url')
        step = Step.objects.create()
        ingred = Ingredient.objects.create()
        step.text = step_text
        ingred.name = ingredient_name
        ingred.units = unit_name
        ingred.quantity = unit_amount
        step.recipe.set(Recipe.objects.filter(id=recid))
        ingred.recipe.set(Recipe.objects.filter(id=recid))
        newRecipe.writer = request.user
        newRecipe.save()
        ingred.save()
        step.save()
        return HttpResponseRedirect(reverse('recipe', args=[recid]))
    else:
        return render(request, "recipeSubmission.html", {})


def delete_ingredient(request, ingredient_id, recipe_id):
    ingredient = get_object_or_404(Ingredient, pk=ingredient_id)
    ingredient.delete()
    return HttpResponseRedirect(reverse('recipe', args=[recipe_id]))


def delete_step(request, step_id, recipe_id):
    step = get_object_or_404(Step, pk=step_id)
    step.delete()
    return HttpResponseRedirect(reverse('recipe', args=[recipe_id]))


def recipeView(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if 'name_change' in request.POST:
        recipe.recipeTitle = request.POST.get('name_change')
        recipe.save()
        return render(request, "recipe.html", context={"recipe": recipe})
    if 'tag_add' in request.POST:
        tag = Tag.objects.create()
        tag.tag = request.POST.get('tag_add').title()  # .title() normalizes capitalization to Title Case
        tag.recipe.set(Recipe.objects.filter(id=recipe_id))
        tag.save()
        recipe.save()
        return render(request, "recipe.html", context={"recipe": recipe})
    try:
        steps_select = recipe.step_set.all()
        ingredient_select = recipe.step_set.all()
        meal_type_select = recipe.meal_type_set.all()
        cuisine_type_select = recipe.cuisine_type_set.all()
        total_likes = recipe.total_likes()
    except(KeyError, recipe.DoesNotExist):
        return render(request, "home.html", {})
    else:
        return render(request, "recipe.html", context={"recipe": recipe, "author": recipe.writer})


def feed_view(request):
    sort_by = "id"
    if request.method == 'GET' and 'sort' in request.GET:
        sort_by = request.GET['sort']
    if request.method == 'GET' and 'r' in request.GET:
        sort_by = "-" + sort_by

    if sort_by == "likes":
        all_recipes = Recipe.objects.annotate(q_count=Count('likes')).order_by('-q_count')
    else:
        all_recipes = Recipe.objects.all().order_by(sort_by)
    return render(request, "feed.html", context={"recipes": all_recipes, "sort": sort_by})


def fork(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe2 = get_object_or_404(Recipe, pk=recipe_id)
    recipe.pk = None
    recipe.writer = User.objects.get(username=request.user)
    recipe.save()
    recipe.parentRecipe = recipe2
    recipe.save()
    for step in recipe2.step_set.all():
        step.pk = None
        step.save()
        step.recipe.set(Recipe.objects.filter(id=recipe.id))
        step.save()
    for ingredient in recipe2.ingredient_set.all():
        ingredient.pk = None
        ingredient.save()
        ingredient.recipe.set(Recipe.objects.filter(id=recipe.id))
        ingredient.save()
    return HttpResponseRedirect(reverse('recipe', args=(recipe.id,)))
