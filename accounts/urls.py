from django.urls import path, re_path
from .views import index

app_name = 'Account'

urlpatterns = [
    path('', index)
]