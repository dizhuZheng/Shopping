from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import ProfileForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    """user's profile"""
    user = request.user
    return render(request, 'account/profile.html', {'user':user})

@login_required
def profile_update(request):
    """ update user's profile """
    if request.method != 'POST':
        form = ProfileForm()
    else:
        form = ProfileForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            authenticated_user = authenticate(username=new_user.username,
            password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('myaccount:profile'))
    context = {'form': form}
    return render(request, 'account/profile_update.html', context)
