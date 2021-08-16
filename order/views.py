from django.shortcuts import render


def cart_details(request):
    return render(request, "order/shoping-cart.html")


def checkout(request):
    return render(request, "order/checkouts.html")


def my_order(request):
    return render(request, "order/my-order.html")
