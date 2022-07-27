from django.shortcuts import render
from django.db.models import Count, Q
from django.views.generic import ListView

from orders.models import Order
from product.models import Product

def home(request):
    order = Order.objects.all()
    order_pending = Order.objects.filter( billing_status = False)
    order_confirmed = Order.objects.filter( billing_status = True)

    context = {
        'orders': order,
        'orders_pending' : order_pending,
        'order_confirmed' : order_confirmed
    }
    return render(request, 'controllers/dashboard.html', context)

class OrderListView(ListView):
    model = Order
    template_name = 'controllers/orders.html'
    context_object_name = 'orders'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context[""] = 
        return context
