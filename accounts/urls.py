from django.urls import path, re_path
from .views import AccountView, logout_view, login_view

app_name = 'Account'

urlpatterns = [
    path('<str:slug>', AccountView.as_view(), name='profile'),
    path('logging-out', logout_view, name='logout'),
    path('log-in/', login_view, name='login-view')
]