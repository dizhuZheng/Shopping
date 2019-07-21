from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
logo = 'Welcome to my recipe'
def index(request):
    """The home page for recipes"""
    return render(request, 'recipes/index.html', {'logo': logo})


@login_required
def dishes(request):
    """show all dishes"""
    dishes = Dish.objects.all()
    context = {'dishes': dishes}
    return render(request, 'recipes/dishes.html', context)


@login_required
def dish(request, dish_id):
    """show a single topic and all its entries"""
    dish = Dish.objects.get(id=dish_id)
    context = {'dish': dish}
    return render(request, 'recipes/dish.html', context)
