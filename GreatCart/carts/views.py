from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem
from django.core.paginator import Paginator

# Create your views here.
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
            cart_id =_cart_id(request),
            
        )
        cart.save()
    
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            cart=cart,
            quantity=1,
            is_active=True
            
        )
        cart_item.save()
    return redirect('cart')
    
def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
    except object.DoesNotExist:
        pass
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items
        
        
    }
    return render(request, 'store/cart.html', context)
def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_items = CartItem.objects.get(product=product, cart=cart)
    if cart_items.quantity > 1:
        cart_items.quantity -= 1
        cart_items.save()
        
    else:
        cart_items.delete() 
    return redirect('cart')   
        
        
        

 