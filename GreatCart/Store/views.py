from django.shortcuts import render,get_object_or_404
from .models import Product
from .models import Category
from django.core.paginator import Paginator

# Create your views here.
def store(request, category_slug=None):
  
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        count = products.count()
    else:
        products = Product.objects.filter(is_available=True)
        paginator = Paginator(products, 6)
        page =request.Get('page')
        paged_product = paginator.get_page(page)
        count = products.count()
        
  
    return render(request, 'store/store.html', locals())

def product_details(request,category_slug,product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
      
    except Exception as e:
        raise e
    context = {
        'single_product':single_product
    }
       
       
 
   
   
    return render(request, 'store/product_details.html', context)


