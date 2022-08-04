from django.views.generic import DetailView, ListView
from django.db.models import Q
from django.shortcuts import render
from product import models

from product.models import Product

def home(request):
    product = {
        'products':Product.objects.all().order_by('-id')[:4],
        'fav_items':Product.objects.all().order_by('-visited')[:6]
    }
    return render(request, 'product/index.html', product)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'].countVisitor()
        context["products"] = Product.objects.all().order_by('-last_visit')[:4]
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'product/list.html'
    context_object_name = 'products'
    ordering = ['-created_by']

    def get_queryset(self):
        if self.kwargs.get('pk'):
            return models.Product.objects.filter(sub_cate = self.kwargs.get('pk'))

        if self.request.method == "GET":
            lookups = Q(name__contains  = self.request.GET.get('search')) | Q(price__contains  = self.request.GET.get('search'))
            return models.Product.objects.filter(lookups)

        else:
            return models.Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["searched_for"] = self.request.GET.get('search')
        return context



