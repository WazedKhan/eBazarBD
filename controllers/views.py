from django.shortcuts import render
from django.db.models import Count, Q
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.views.generic import ListView, CreateView


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


class ProductCreateView(CreateView):
    model = Product
    template_name = 'controllers/product/create.html'
    fields = ['name','price','discount','sub_cate','brand_name','image']
    success_url	= reverse_lazy('admin-home')

    def form_valid(self, form):
        form.instance.created_by = self.request.user

        return super(ProductCreateView, self).form_valid(form)

