from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from product.models import Product
from .cart import Cart

# Create your views here.
def add_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        productId = request.POST.get('productId')
        quantity = request.POST.get('quantity')
        product = get_object_or_404(Product, id = productId)
        cart.add(product, quantity)
        return JsonResponse({'data':'saved'})
    return JsonResponse({'ok':'ok'})