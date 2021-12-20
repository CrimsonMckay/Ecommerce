from .models import Category

# A context processor is just a python function that takes one arguement which is an http request object
def menu_links(request):
    links=Category.objects.all()
    return dict(links=links) #each context processor function must return  dictionary and it will be available anywhere in our code