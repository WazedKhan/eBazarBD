from django.urls import path
from controllers import views

urlpatterns = [
    path('', views.home, name='admin-home')
]