from django.urls import path


from admins.views import index, users, categories, products


app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users', users, name='users'),
    path('categories', categories, name='categories'),
    path('products', products, name='products'),
]
