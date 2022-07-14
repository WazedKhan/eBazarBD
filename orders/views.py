from decimal import Decimal
from multiprocessing import context
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from cart.cart import Cart
from orders.models import Order, OrderItem

# Create your views here.
def add(request):
    cart = Cart(request)
    context = {
        'user':User,
        'total_price':cart.final_price
    }
    return render(request, 'orders/info.html', context)


def place(request):
    cart = Cart(request)
    if request.method == 'POST':
        name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        post_code = request.POST.get('post_code')

        Order.objects.create(
            full_name = name,
            phone = phone,
            address = address,
            post_code = post_code,
            total_paid = Decimal(cart.final_price()),
        )

    return JsonResponse({"Status ":200, 'total_price':cart.final_price(),})