from django.http import HttpResponse
from django.shortcuts import render

from product.models import Product

def home(request):
    product = {
        'products':Product.objects.all()
    }
    return render(request, 'product/index.html', product)