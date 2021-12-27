from django.db.models.fields import SlugField
from django.shortcuts import get_object_or_404, render , redirect
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

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )  
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart
        )                 
        cart_item.save()
        
    return redirect('cart_detail')    

def cart_detail(request, total=0 , counter=0 , cart_items = None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart , active =True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
            
    except ObjectDoesNotExist:
        pass
    
    return render(request, 'cart.html' , dict(cart_items = cart_items , total = total , counter =counter))           
    
    
# Create your views here.
 