from django.shortcuts import render

from .models import Product, ProductCategory


def index(request):
    context = {
        'title': 'GeekShop - Главная',
    }
    return render(request, 'products/index.html', context)


def products(request):

    products = Product.objects.all()
    categories = ProductCategory.objects.all()

    context = {
        'products': products,
        'categories': categories,

        'title': 'GeekShop - Каталог',
    }
    return render(request, 'products/products.html', context)
