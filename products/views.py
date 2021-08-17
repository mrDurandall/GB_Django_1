from django.shortcuts import render

import json

from .models import Product, ProductCategory


def index(request):
    context = {
        'username': 'Турганов И.Д.',
        'title': 'GeekShop - Главная',
    }
    return render(request, 'products/index.html', context)


def products(request):
    # with open('products/fixtures/products.json', encoding='utf-8') as json_prod:
    #     products = json.load(json_prod)

    products = Product.objects.all()
    categories = ProductCategory.objects.all()

    context = {
        'products': products,
        'categories': categories,

        'title': 'GeekShop - Каталог',
    }
    return render(request, 'products/products.html', context)

