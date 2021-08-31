from django.urls import path


from admins.views import index, users, categories, products, user_create, user_update, user_delete, user_restore
from admins.views import category_add, category_edit, category_delete

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users', users, name='users'),
    path('user_create', user_create, name='user_create'),
    path('user_update/<int:id>', user_update, name='user_update'),
    path('user_delete/<int:id>', user_delete, name='user_delete'),
    path('user_restore/<int:id>', user_restore, name='user_restore'),
    path('categories', categories, name='categories'),
    path('category_add', category_add, name='category_add'),
    path('category_edit/<int:id>', category_edit, name='category_edit'),
    path('category_delete/<int:id>', category_delete, name='category_delete'),
    path('products', products, name='products'),

]
