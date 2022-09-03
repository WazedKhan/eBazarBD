from orders.models import Order, OrderItem
from django.shortcuts import render
from product.models import Product
from accounts.models import User
from .models import Seller

from django.views.generic import ListView

# Create your views here.
def index(request):
    user = request.user
    seller = Seller.objects.get(user = user)
    orderItems = OrderItem.objects.all()
    products = Product.objects.all()
    most_visited_products = 0
    in_progress_items = 0
    confirmed_items = 0
    count_product = 0

    for item in orderItems:
        if item.product.created_by.user == user and item.order.billing_status == True:
            confirmed_items += 1

    for item in orderItems:
        if item.order.billing_status == False and item.product.created_by.user == user:
            in_progress_items += 1

    for product in products:
        if product.created_by.user == user:
            count_product += 1

    context = {
        'products' : count_product,
        'confirmed_items' : confirmed_items,
        'in_progress_items': in_progress_items,
        'most_visited_products': Product.objects.filter(created_by = seller).order_by('-visited')
    }
    print('--------------------------------------------------------------------------------------------------')
    print('Dashboard View')
    print(most_visited_products)
    print('--------------------------------------------------------------------------------------------------')
    return render(request, 'sellers/dashboard.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'sellers/product/list.html'