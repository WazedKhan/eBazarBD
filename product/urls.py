from django.urls import path
from product import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-details'),
]
