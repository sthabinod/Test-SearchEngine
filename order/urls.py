from django.urls import path
from . import views

urlpatterns = [
    path('cart-details', views.cart_details, name="cart-details"),
    path('checkout', views.checkout, name="checkout"),
    path('my-order', views.my_order, name="my-order")
]
