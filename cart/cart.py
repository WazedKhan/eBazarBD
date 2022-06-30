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


    def add(self, product, qty):
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['quantity'] = qty
        else:
            self.cart[product_id] = {'price': str(product.price), 'quantity': qty}

        self.save()


    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def save(self):
        self.session.modified = True