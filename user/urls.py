from django.urls import path

from user import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.registetion, name='register'),
]