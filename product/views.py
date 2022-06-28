from django.views.generic import DetailView
from django.shortcuts import render

from product.models import Product

def home(request):
    product = {
        'products':Product.objects.all()
    }
    return render(request, 'product/index.html', product)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context
