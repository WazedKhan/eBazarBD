from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout

from accounts.models import User

# Create your views here.
class AccountView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = User
    template_name = 'user/index.html'


def logout_view(request):
    logout(request)

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            ...
        else:
            # Return an 'invalid login' error message.
            ...
    else:
        return render(request ,'user/login.html')