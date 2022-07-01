from decimal import Decimal
from django.contrib.sessions.models import Session

from product.models import Product

class Cart():

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('s_key')
        if 's_key' not in request.session:
            cart = self.session['s_key'] = {}
        self.cart = cart
        try:
            s_id = request.session._session_key
            print(Session.objects.get(pk = s_id).get_decoded())
        except:
            print('Session is not set yet')


    def add(self, product, qty):
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['quantity'] = qty
        else:
            self.cart[product_id] = {'price': str(product.price), 'quantity': qty}

        self.save()


    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())


    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in = product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['sub_total'] = Decimal(item['price']) * Decimal(item['quantity'])
            yield item


    def remove(self, productId):
        productId = str(productId)
        if productId in self.cart:
            del self.cart[productId]
            self.save()


    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def final_price(self):
        total_price = self.get_total_price()
        return total_price + 50

    def products(self):
        return len(self.cart.keys())


    def save(self):
        self.session.modified = True