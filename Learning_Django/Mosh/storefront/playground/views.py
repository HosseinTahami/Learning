from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, Order


def say_hello(request):
    queryset = Product.objects.filter(unit_price__range=((20, 100)))
    return render(request, 'hello.html', {'name': 'Hossein', 'products': list(queryset)})
