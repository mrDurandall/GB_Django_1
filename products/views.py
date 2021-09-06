from django.shortcuts import render

from .models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    context = {
        'title': 'GeekShop - Главная',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    context = {}
    if category_id:
        products = Product.objects.filter(category_id=category_id)
        context.update({'category_id': category_id})
    else:
        products = Product.objects.all()

    paginator = Paginator(products, per_page=3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    categories = ProductCategory.objects.all()
    context.update({
        'products': products_paginator,
        'categories': categories,
        'title': 'GeekShop - Каталог',
    })
    return render(request, 'products/products.html', context)
