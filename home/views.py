from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Recipe, Favorite


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


def submit_recipe(request):
    if (request.method == "POST"):
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
