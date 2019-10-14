from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import ProfileForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import send_mail
from django.contrib.auth.models import User
# from .forms import SignupForm

@login_required
def profile(request):
    """user's profile"""
    user = request.user
    return render(request, 'myaccount/profile.html', {'user':user})

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

@login_required
def send_pwd_change_email(request):
    """send emails to user to change pwd"""
    res = send_mail('hello topher', 'HAHAHAHA', 'dizhu210@gmail.com', 'karl9242@gmail.com', fail_silently=False)
    return HttpResponse('%s'%res)


# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             message = render_to_string('acc_active_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': account_activation_token.make_token(user),
#             })
#             mail_subject = 'Activate your account'
#             to_email = form.cleaned_data.get('email')
#             email = EmailMessage(mail_subject, message, to=[to_email])
#             email.send()
#             return HttpResponse('Please')
#     else:
#         form = SignupForm()

#     return render(request, 'signup.html', {'form': form})
