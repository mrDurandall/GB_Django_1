from django.urls import path
from django.views.decorators.cache import cache_page

from products.views import IndexTemplateView, ProductsListView, CategoryProductsListView


app_name = 'products'

urlpatterns = [
    path('', cache_page(3600)(ProductsListView.as_view()), name='product'),
    path('<int:category_id>', CategoryProductsListView.as_view(), name='category'),
]
