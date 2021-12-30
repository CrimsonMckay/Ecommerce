from .models import Category
from .models import CartItem,Cart
from .views import _cart_id
# A context processor is just a python function that takes one arguement which is an http request object
def menu_links(request):
    links=Category.objects.all()
    return dict(links=links) #each context processor function must return  dictionary and it will be available anywhere in our code

def cart_page(request):
    cart_links=CartItem.objects.all()
    return dict(cart_links=cart_links)
    
def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
      try:
          cart = Cart.objects.filter(cart_id=_cart_id(request))
          cart_items = CartItem.objects.all().filter(cart=cart[:1])
          for cart_item in cart_items:
              item_count += cart.quantity
      except Cart.DoesNotExist:
        item_count=0
    return dict(item_count=item_count)    

def overall_total(request):
        total=0
        if 'admin' in request.path:
            return {}
        else:
          try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart , active =True)
            for cart_item in cart_items:
              total += (cart_item.product.price * cart_item.quantity)
          except  Cart.DoesNotExist:
              total=0
        return dict(total=total)      