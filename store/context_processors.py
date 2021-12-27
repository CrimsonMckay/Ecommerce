from .models import Category
from .models import CartItem
from . import views
# A context processor is just a python function that takes one arguement which is an http request object
def menu_links(request):
    links=Category.objects.all()
    return dict(links=links) #each context processor function must return  dictionary and it will be available anywhere in our code

def cart_page(request):
    cart_links=CartItem.objects.all()
    return dict(cart_links=cart_links)
    