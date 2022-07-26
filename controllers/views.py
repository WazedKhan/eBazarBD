from django.shortcuts import render
from django.db.models import Count, Q

from orders.models import Order

def home(request):
    order = Order.objects.all()
    order_pending = Order.objects.filter( billing_status = False)
    order_confirmed = Order.objects.filter( billing_status = True)

    context = {
        'orders': order,
        'orders_pending' : order_pending,
        'order_confirmed' : order_confirmed
    }
    return render(request, 'controllers/base.html', context)