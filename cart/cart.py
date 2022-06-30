from django.contrib.sessions.models import Session

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


    def add(self, product, quantity):
        productId = product.id
        self.quantity = int(quantity)
        print(type(self.quantity))
        if productId not in self.cart:
            self.cart[productId] = {'price':product.price, 'quantity':quantity}
        elif productId in self.cart:
            self.cart[productId]['quantity'] += self.quantity
        print(self.__len__())
        self.session.modified = True


    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())