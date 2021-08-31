from django.urls import path


from admins.views import index, users, categories, products, user_create, user_update, user_delete, user_restore


app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users', users, name='users'),
    path('user_create', user_create, name='user_create'),
    path('user_update/<int:id>', user_update, name='user_update'),
    path('categories', categories, name='categories'),
    path('products', products, name='products'),
    path('user_delete/<int:id>', user_delete, name='user_delete'),
    path('user_restore/<int:id>', user_restore, name='user_restore'),
]
