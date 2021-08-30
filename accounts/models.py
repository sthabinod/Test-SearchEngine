from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        managed = True
        verbose_name = 'Customers'
        verbose_name_plural = 'Customers'

    def __str__(self) -> str:
        return self.address

    def get_absolute_url(self):
        return f'/{self.slug}/'
