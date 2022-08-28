from django.shortcuts import render
from accounts.models import User
from orders.models import Order, OrderItem
from product.models import Product

# Create your views here.
def index(request):
    user = request.user
    orderItems = OrderItem.objects.all()
    products = Product.objects.all()
    ordered = 0
    count_product = 0

    for item in orderItems:
        if item.product.created_by.user == request.user:
            ordered += 1

    for product in products:
        if product.created_by.user == request.user:
            count_product += 1

    context = {
        'products' : count_product,
        'ordered_number' : ordered
    }
    print('--------------------------------------------------------------------------------------------------')
    print("info's")
    print('--------------------------------------------------------------------------------------------------')
    return render(request, 'sellers/dashboard.html', context)