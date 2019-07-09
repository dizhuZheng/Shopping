from django.shortcuts import render
from .models import Image
# Create your views here.
def index(request):
    """The home page for learning log"""
    return render(request, 'recipes/index.html')
