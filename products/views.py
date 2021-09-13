from .models import Product, ProductCategory
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView

from common.views import CommonContextMixin


class IndexTemplateView(CommonContextMixin, TemplateView):

    template_name = 'products/index.html'
    title = 'GeekShop - Главная'


class ProductsListView(ListView):

    model = Product
    template_name = 'products/products.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['title'] = 'GeekShop - Каталог'
        return context


class CategoryProductsListView(ProductsListView):

    def get_queryset(self):
        self.category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=self.category_id)
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryProductsListView, self).get_context_data(**kwargs)
        context['category_id'] = self.category_id
        context['title'] = f'GeekShop - Каталог :: {ProductCategory.objects.get(id=self.category_id)}'
        return context

