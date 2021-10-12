from django.db import models
from django.utils.functional import cached_property

# Create your models here.
from user.models import User
from products.models import Product


class BasketQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super(BasketQuerySet, self).delete(*args, **kwargs)


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity

    @cached_property
    def get_items_cached (self):
        return self.user.basket.select_related()

    def total_quantity(self):

        _items = self.get_items_cached
        return sum(list(map(lambda i: i.quantity, _items)))
        # baskets = Basket.objects.filter(user=self.user)
        # return sum(basket.quantity for basket in baskets)

    def total_price(self):
        # baskets = Basket.objects.filter(user=self.user)
        # return sum(basket.sum() for basket in baskets)
        _items = self.get_items_cached
        return sum(list(map(lambda i: i.quantity * i.product.price, _items)))

    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()

