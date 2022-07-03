from django.urls import path
from product import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-details'),
    path('products/list/<int:pk>', views.ProductListView.as_view(), name='list-view'),
    path('products/list/', views.ProductListView.as_view(), name='list-view'),
]
