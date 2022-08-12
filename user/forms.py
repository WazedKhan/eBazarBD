from django import forms
from user.models import Client
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model= User
        fields = ['username', 'first_name', 'email', 'password1','password2']
