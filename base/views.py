from django.shortcuts import render
from product.models import Category, Product
import datetime
from .models import Information


def index(request):
    three_days_a_head = datetime.datetime.now() - datetime.timedelta(days=3)

    information = Information.objects.get(id=1)
    categories = Category.objects.all()[:12]
    products = Product.objects.all()
    latest_product = Product.objects.filter(
        date_added__gte=three_days_a_head)[:3]

    expensive_product = Product.objects.filter(
        price__gte=300)[:3]

    cheapest_product = Product.objects.filter(
        price__lte=100)[:3]

    data = {
        'categories': categories,
        'products': products,
        'latest_product': latest_product,
        'cheapest_product': cheapest_product,
        'expensive_product': expensive_product,
        'information': information,
    }

    if request.method == "POST":
        print("POST REQUEST")
        search = request.POST.get("search")
        search_query = Product.objects.filter(name__contains=search)
        print(search_query)
        data['search'] = search_query
    else:
        print("No POST REQUEST..")

    return render(request, 'index.html', data)


def contact(request):
    return render(request, 'contact.html')
