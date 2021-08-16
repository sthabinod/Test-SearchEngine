from django.shortcuts import render
from .models import Product, Category


def shop_details(request, id):
    query = Product.objects.get(id=id)
    print(query.category)
    related = Product.objects.filter(category=query.category).exclude(id=id)
    data = {
        'details': query,
        'related': related,
    }
    return render(request, "shop-details.html", data)


def all_goods(request):
    query = Product.objects.all()
    data = {
        'products': query,
    }
    return render(request, "shop-grid.html", data)
