from django.urls import path

from admins.views import AdminIndexView
from admins.views import UsersListView, UserCreateView, UserUpdateView, UserDeleteRestoreView
from admins.views import CategoriesListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView
from admins.views import ProductsListView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'admins'

urlpatterns = [
    path('', AdminIndexView.as_view(), name='index'),
    path('users', UsersListView.as_view(), name='users'),
    path('user_create/', UserCreateView.as_view(), name='user_create'),
    path('user_update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user_delete_restore/<int:pk>/', UserDeleteRestoreView.as_view(), name='user_delete_restore'),
    path('categories', CategoriesListView.as_view(), name='categories'),
    path('category_add/', CategoryCreateView.as_view(), name='category_add'),
    path('category_edit/<int:pk>/', CategoryUpdateView.as_view(), name='category_edit'),
    path('category_delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('products', ProductsListView.as_view(), name='products'),
    path('product_add', ProductCreateView.as_view(), name='product_add'),
    path('product_edit/<int:pk>', ProductUpdateView.as_view(), name='product_edit'),
    path('product_delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
]
