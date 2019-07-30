from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
logo = 'Welcome to my Recipe'
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
    """show a single topic"""
    dish = Dish.objects.get(id=dish_id)
    context = {'dish': dish}
    return render(request, 'recipes/dish.html', context)

@login_required
def upload_img(request):
    if request.method == 'POST':
        new_img = IMG(
            img = request.FILES.get('img'),
            name = request.FILES.get('img').name
        )
        new_img.save()
    return render(request, 'recipes/upload.html')

@login_required
def show_img(request):
    """show pics"""
    imgs = IMG.objects.all()
    content = {
        'imgs':imgs,
    }
    for i in imgs:
        print (i.img.url)
    return render(request,'recipes/show.html',content)
