from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from product.models import Product
from .cart import Cart
from cart import cart

# Create your views here.
def add_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        productId = request.POST.get('productId')
        quantity = int(request.POST.get('quantity'))
        product = get_object_or_404(Product, id = productId)
        cart.add(product, quantity)
        return JsonResponse({'quantity':cart.__len__()})
    return JsonResponse({'ok':'ok'})


def list(request):
    cart = Cart(request)
    return render(request, 'cart/list.html', {'cart':cart})


def remove(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        productId = request.POST.get('productid')
        cart.remove(productId)

        return JsonResponse({
            'final_price':cart.final_price(),
            'total_price':cart.get_total_price(),
            'product_numbers':cart.products(),
            'quantity':cart.__len__(),
            })