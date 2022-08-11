from django import forms
from user.forms import UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    return render(request, 'user/index.html')

def registetion(request):
    # if request.user.is_authenticated:
    #     return redirect('home')

    if request.POST:
        form = UserRegisterForm(request.POST)
        print(request.POST.get('phone'))
        if form.is_valid():
            user = form.save()
            print(user)
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form':form})