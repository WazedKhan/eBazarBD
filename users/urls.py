from django.urls import path

from users import views

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('login', views.loginView, name='login'),
]
