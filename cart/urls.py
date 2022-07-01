from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
    path('add/', views.add_cart, name='add_cart'),
    path('list/', views.list, name='list'),
    path('list/remove', views.remove, name='remove'),
]
