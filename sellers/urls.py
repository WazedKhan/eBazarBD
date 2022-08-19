from django.urls import path
from .views import index

app_name = 'Seller'

urlpatterns = [
    path('', index, name='seller-home')
]