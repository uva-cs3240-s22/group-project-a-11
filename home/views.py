from django.shortcuts import render

# Create your views here.
def home_view(request):
    """
      View for home page.
    """
    return render(request, "home.html", {})
