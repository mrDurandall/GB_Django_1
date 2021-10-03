from django.urls import path

from orders.views import OrderListView,\
    OrderCreateView,\
    OrderUpdateView, OrderDeleteView, order_complete


app_name = 'orders'

urlpatterns = [
    path('/', OrderListView.as_view(), name='index'),
    path('new/', OrderCreateView.as_view(), name='new'),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', OrderDeleteView.as_view(), name='delete'),
    path('complete/<int:pk>/', order_complete, name='complete'),

]

