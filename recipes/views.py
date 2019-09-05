from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .models import *
from .forms import DishForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.
logo = 'Welcome to my Recipe'
sentence = 'picture uploaded !'

def index(request):
    """The home page for recipes"""
    return render(request, 'recipes/index.html', {'logo': logo})


def categories(request):
    """show all categories"""
    categories = Category.objects.all()
    return render(request, 'recipes/categories.html', {'category': category})

def category(request, pk):
    category = Category.objects.get(pk=pk)
    return render(request, 'recipes/category.html', {'category': category})


@login_required
def dish(request, dish_id):
    """show a single topic"""
    dish = Dish.objects.get(id=dish_id)
    content = {'dish':dish}
    if request.method == 'POST':
        new_img = IMG(
            img = request.FILES.get('img'),
            name = request.FILES.get('img').name
        )
        new_img.save()
        content['sentence']= sentence
    return render(request, 'recipes/dish.html', content)


@login_required
def new_dish(request):
    """add a new dish"""
    if request.method != 'POST':
        #no data submitted, create a blank form
        form = DishForm()

    else:
        #POST data submitted, process data
        form = DishForm(request.POST)
        if form.is_valid():
            new_dish = form.save(commit=False)
            new_dish.owner = request.user
            new_dish.save()
            return HttpResponseRedirect(reverse('recipes:dishes'))

    context = {'form': form}
    return render(request, 'recipes/new_dish.html', context)
