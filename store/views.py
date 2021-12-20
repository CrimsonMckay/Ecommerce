from django.db.models.fields import SlugField
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Category, Product , Cart , CartItem
from  django.core.exceptions import ObjectDoesNotExist


def home(request, category_slug=None):#category slug to retrieve corresponding category
    category_page = None
    products = None
    if category_slug!=None:
        category_page = get_object_or_404(Category,slug=category_slug)#Assign the result of corresponding object to category_page
        products = Product.objects.filter(category=category_page, available=True) #retrive product objects from database base on category... we use the filter function to narrow down our query result based on Category page parameter
    else:
        products =Product.objects.all().filter(available=True)  
        
    return render(request,'home.html', {'category':category_page,'products': products})


def productPage(request,category_slug,product_slug):
    
    try:
        product=Product.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception as e:
         raise e
    
    return render(request,'product.html', {'product':product})


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product_id, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart
        )                 
        cart_item.save()
        
    return redirect('cart_detail')    
# Create your views here.
 