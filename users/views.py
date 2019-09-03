from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.decorators import login_required
from .form import CustomUserCreationForm

# Create your views here.
def logout_view(request):
    """log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('recipes:index'))

@login_required
def personal(request):
    # context = {'username': username}
    return render(request, 'users/personal_space.html')

def register(request):
    """register new user"""
    if request.method != 'POST':
        form = CustomUserCreationForm()
    else:
        #process completed form.
        form = CustomUserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,
            password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('recipes:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)
