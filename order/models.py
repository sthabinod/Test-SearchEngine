from django.db import models
from product.models import Product
from accounts.models import Customer


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    order_address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    order_date = models.DateTimeField()
    order_status = models.BooleanField()
    slug = models.SlugField()

    class Meta:
        managed = True
        verbose_name = 'Orders'
        verbose_name_plural = 'Orders'

    def __str__(self) -> str:
        return "Order " + self.id

    def get_absolute_url(self):
        return f'/{self.slug}/'
