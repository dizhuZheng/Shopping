from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileForm(forms.Form):
   first_name = forms.CharField(label='First Name', max_length=50, required=True)
   last_name = forms.CharField(label='Last Name', max_length=50, required=True)
   org = forms.CharField(label='Organization', max_length=50, required=False)
   telephone = forms.CharField(label='Tele', max_length=50, required=False)
