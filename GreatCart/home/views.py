from django.shortcuts import render
from Store.models import Product

# Create your views here.
def homes(request):
    products = Product.objects.filter(is_available=True)
    
    return render(request, 'home/index.html', locals())
