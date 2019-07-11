from django.shortcuts import render
from .models import *

# Create your views here.
logo = 'Welcome to my recipe'
def index(request):
    """The home page for recipes"""
    return render(request, 'recipes/index.html', {'logo': logo})
