from django.urls import path
from controllers import views

urlpatterns = [
    path('', views.home, name='admin-home'),
    path('orders', views.OrderListView.as_view(), name='order-list'),
    path('create-product', views.ProductCreateView.as_view(), name='product-create'),
]