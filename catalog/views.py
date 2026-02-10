from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product


# ======================================
# الصفحة الرئيسية
# ======================================
def home(request):
    products = Product.objects.filter(is_active=True).order_by('-id')[:6]
    return render(request, 'home.html', {
        'products': products,
    })


# ======================================
# صفحة الكتالوج
# ======================================
def catalog_view(request):
    categories = Category.objects.filter(is_active=True)
    products = Product.objects.filter(is_active=True)

    return render(request, 'catlog-t/catalog.html', {
        'categories': categories,
        'products': products,
    })


# ======================================
# إضافة منتج للسلة
# ======================================
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': float(product.price),
            'image': product.image.url,
            'quantity': 1,
        }

    request.session['cart'] = cart
    request.session.modified = True

    return redirect(request.META.get('HTTP_REFERER', 'home'))


# ======================================
# عرض السلة
# ======================================
def cart_view(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())

    return render(request, 'cart.html', {
        'cart': cart,
        'total': total,
    })


# ======================================
# حذف منتج من السلة
# ======================================
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
        request.session.modified = True

    return redirect('cart')
