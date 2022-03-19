from django.shortcuts import render

# Create your views here.
def home_view(request):
    """
      View for home page.
    """
    return render(request, "home.html", {})


def template_testing_view(request):
    """
    A view to allow templates to be created before the backend is ready
    Should be removed for final release
    Written by Ben
    """
    template_to_test = "recipe.html"
    return render(request, template_to_test, {})