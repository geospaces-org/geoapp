import json
from mangorest import mango

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("settings.CART_SESSION_ID")
        if not cart:
            cart = self.session["settings.CART_SESSION_ID"] = {}
        self.cart = cart

    def __iter__(self):
        cart = self.cart.copy()
        for item in cart.values():
            item['price'] = item['price']
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())

    def add(self, product_id, qty=1, price=0.01, name="", img="", override_quantity=False):
        if product_id not in self.cart:
            self.cart[product_id] = {'id': product_id, 'qty': 0, 'price': price, 'name': name, 'img': img}

        print ("+++",self.cart)

        if override_quantity:
            self.cart[product_id]['qty'] = qty
        else:
            self.cart[product_id]['qty'] += qty
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        self.cart = self.session["settings.CART_SESSION_ID"] = {}
        self.save()

    @property
    def get_total_price(self):
        return sum(item['price'] * item['qty'] for item in self.cart.values())

    @property
    def str(self):
        items = [k.copy() for k in self.cart.values()]
        sum = 0
        for c in items:
            c["cost"] = float(c['price'] * c['qty'])
            sum += c["cost"]
        ret = {
            'items': items,
            'total': sum
        }
        ret = json.dumps(ret, cls=mango.myEncoder)
        return ret

#---------------------------------------------------------------------------------
def cartcontext(request):
    return {'cart': Cart(request)}
#---------------------------------------------------------------------------------
from django.http import HttpResponse, JsonResponse
from mangorest import mango
def _updatecart(request, id=None, name="", img="", price= 0, qty= 0,override=0, **kwargs ):
    cart = Cart(request)
    if (id):
        if(qty == 0):
            cart.remove(id)
        else:
            cart.add(id, int(qty), float(price),name,img, int(override) )

    ret = cart.str
    return ret

from django.views.decorators.csrf import csrf_exempt
#@csrf_exempt
def updatecart(request):
    par = mango.getparms(request)
    ret = _updatecart(request, **par)
    print (f'return: {ret}')
    return HttpResponse(ret)

@csrf_exempt
def clearcart(request):
    cart = Cart(request)
    cart.clear()
    return HttpResponse(cart.str)
#---------------------------------------------------------------------------------
