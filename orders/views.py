from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from catalog.models import Product
from .models import Cart, CartItem


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_active=True)

    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        cart_item.quantity += 1
    cart_item.save()

    messages.success(request, "تمت إضافة المنتج إلى السلة 🛒")
    return redirect(request.META.get('HTTP_REFERER', 'cart_detail'))


@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.select_related('product')

    total = sum(item.product.price * item.quantity for item in items)

    context = {
        'cart': cart,
        'items': items,
        'total': total
    }
    return render(request, 'orders-t/cart.html', context)


@login_required
def remove_from_cart(request, item_id):
    cart = get_object_or_404(Cart, user=request.user)
    item = get_object_or_404(CartItem, id=item_id, cart=cart)
    item.delete()

    messages.success(request, "تم حذف المنتج من السلة ❌")
    return redirect('cart_detail')
