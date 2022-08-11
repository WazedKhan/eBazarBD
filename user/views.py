from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


@login_required
def profile(request):
    return render(request, 'user/index.html')

def registetion(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            print(username)
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form':form})