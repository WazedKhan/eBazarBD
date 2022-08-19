from django.shortcuts import render
from product.models import Product

# Create your views here.
def index(request):
    context = {
        'products' : Product.objects.first()
    }
    return render(request, 'sellers/base.html', context)