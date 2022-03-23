from django.shortcuts import render


# Create your views here.
def home_view(request):
    """
      View for home page.
    """
    return render(request, "home.html", {})


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