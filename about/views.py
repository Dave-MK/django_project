from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about_me(request):
    """
    Render the about me page.
    """
    return HttpResponse(
        "About Me"
    )