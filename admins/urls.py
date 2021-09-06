from django.urls import path

from admins.views import AdminIndexView
from admins.views import UsersListView, UserCreateView, UserUpdateView, UserDeleteView, UserRestoreView
from admins.views import categories, category_add, category_edit, category_delete
from admins.views import products, product_add, product_edit, product_delete

app_name = 'admins'

urlpatterns = [
    path('', AdminIndexView.as_view(), name='index'),
    path('users', UsersListView.as_view(), name='users'),
    path('user_create', UserCreateView.as_view(), name='user_create'),
    path('user_update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user_delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    path('user_restore/<int:pk>/', UserRestoreView.as_view(), name='user_restore'),
    path('categories', categories, name='categories'),
    path('category_add', category_add, name='category_add'),
    path('category_edit/<int:id>', category_edit, name='category_edit'),
    path('category_delete/<int:id>', category_delete, name='category_delete'),
    path('products', products, name='products'),
    path('product_add', product_add, name='product_add'),
    path('product_edit/<int:id>', product_edit, name='product_edit'),
    path('product_delete/<int:id>', product_delete, name='product_delete'),
]
