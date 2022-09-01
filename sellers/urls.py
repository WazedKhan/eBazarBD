from django.urls import path
from .views import index, ProductListView

app_name = 'Seller'

urlpatterns = [
    path('', index, name='seller-home'),
    path('products', ProductListView.as_view(), name='product-list')
]