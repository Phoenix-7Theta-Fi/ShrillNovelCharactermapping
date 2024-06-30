from .models import Order, OrderItem
from django.db.models import Sum

def get_or_create_cart(request):
    cart_id = request.session.get('cart_id')
    if cart_id:
        cart = Order.objects.filter(id=cart_id, status='cart').first()
        if cart:
            return cart
    cart = Order.objects.create(user=request.user, status='cart')
    request.session['cart_id'] = cart.id
    return cart

def add_to_cart(request, product, quantity):
    cart = get_or_create_cart(request)
    item, created = OrderItem.objects.get_or_create(order=cart, product=product)
    if not created:
        item.quantity += quantity
    else:
        item.quantity = quantity
    item.price = product.price
    item.save()

def remove_from_cart(request, product):
    cart = get_or_create_cart(request)
    OrderItem.objects.filter(order=cart, product=product).delete()

def get_cart_total(cart):
    return cart.orderitem_set.aggregate(total=Sum('price' * 'quantity'))['total'] or 0