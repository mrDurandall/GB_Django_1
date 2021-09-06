from django.urls import path

from products.views import ProductsListView, CategoryProductsListView


app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='product'),
    path('<int:category_id>', CategoryProductsListView.as_view(), name='category'),
]
