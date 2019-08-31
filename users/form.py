from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
import re

class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label="Enter Username", min_length=5, max_length=41, help_text='User name must contain chracters or letters, at least 5, at most 41 characters')
    email = forms.EmailField(label="Enter email", widget=forms.EmailInput, required = True)
    password1 = forms.CharField(label="Enter Password", help_text='Passwords must contain at least 6, must include uppercase, lowercase letters and numbers',
    min_length=6, widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", min_length=6, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        m = re.search('^[a-zA-Z0-9]\w{4,40}$', username)
        if m is None:
            raise forms.ValidationError('Invalid Name, please follow the rules !')
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError('Username already exists !')
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError('Email already exists !')
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        r = re.search('^(?![a-zA-Z]+$)(?![0-9]+$)[0-9A-Za-z]\w{5,17}$', password1)
        if r is None:
            raise forms.ValidationError('Password\'s format is wrong !')
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError('Password don\'t match !')
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user
