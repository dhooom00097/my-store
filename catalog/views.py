from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
from django.shortcuts import render
from .models import Category, Product


def catalog_view(request):
    categories = Category.objects.filter(is_active=True)
    products = Product.objects.filter(is_active=True)

    return render(request, 'catlog-t/catalog.html', {
        'categories': categories,
        'products': products,
    })
