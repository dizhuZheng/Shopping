from django.shortcuts import render
from .models import Image
# Create your views here.
def index(request):
    """The home page for recipes"""
    return render(request, 'recipes/index.html')
