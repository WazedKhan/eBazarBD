from decimal import Decimal
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

from cart.cart import Cart
# models from different apps
from product.models import Product
from orders.models import Order, OrderItem

# Create your views here.
def add(request):
    # sends session cart data to cart list view page
    cart = Cart(request)
    context = {
        'user':User,
        'total_price':cart.final_price
    }
    return render(request, 'orders/info.html', context)


def place(request):
    # creates order to database
    cart = Cart(request)
    if request.method == 'POST':
        name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        post_code = request.POST.get('post_code'),
        totalPrice = Decimal(cart.final_price())

        order = Order.objects.create(
            user = request.user,
            full_name = name,
            phone = phone,
            address = address,
            post_code = post_code,
            total_paid = Decimal(cart.final_price()),
        )

        for item in cart:
            OrderItem.objects.create(
                order = order,
                product = item['product'],
                price = Decimal(item['price']),
                discount = Decimal(1),
                quantity = item['quantity']
            )


        # counts number of product sold after order has been confirm
        for item in cart:
            # Product.objects.get()
            print(item['product'].totalSold(item['quantity']))

        # clears session data
        cart.clear()


        # subject = 'Order Received'
        # from_email = settings.DEFAULT_FROM_EMAIL
        # message = 'This is my test message'
        # recipient_list = ['wazedkhan119399@gmail.com']
        # html_message = f'<h1>Dear {request.user.first_name}</h1>'
        # send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)

    return render(request, 'orders/confirm.html')