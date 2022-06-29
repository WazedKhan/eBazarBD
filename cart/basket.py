from django.contrib.sessions.models import Session
from requests import request, session

class Basket():

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('s_key')
        if 's_key' not in request.session:
            basket = self.session['s_key'] = {}
        self.basket = basket
        
