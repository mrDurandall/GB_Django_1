from django.shortcuts import render

from .models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView


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


class ProductsListView(ListView):

    model = Product
    template_name = 'products/products.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context


class CategoryProductsListView(ProductsListView):

    def get_queryset(self):
        self.category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=self.category_id)
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryProductsListView, self).get_context_data(**kwargs)
        context['category_id'] = self.category_id
        return context

