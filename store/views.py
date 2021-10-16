from django.db.models.fields import SlugField
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Category, Product


def home(request, category_slug=None):
    category_page = None
    products = None
    if category_slug!=None:
        category_page = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category=category_page, available=True)
    else:
        products =Product.objects.all().filter(available=True)  
        
    return render(request,'home.html', {'category':category_page,'products': products})


def productPage(request):
    return render(request,'product.html')

# Create your views here.
 