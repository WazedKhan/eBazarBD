from django.urls import path
from orders import views


urlpatterns = [
    path('add/', views.add, name='order-add'),
    path('place/', views.place, name='order-place')
]
