from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, Order, OrderItem
from django.db.models import Q, F, Value


def say_hello(request):
    queryset_1 = Product.objects.filter(unit_price__range=((20, 100)))
    queryset_2 = Product.objects.filter(
        title__icontains="Cof").order_by('title')
    queryset_3 = Order.objects.filter(
        orderitem__product__title__icontains="coff").order_by('id').reverse()

    # Q--> or:| , and:& , ~:not
    queryset_4 = Product.objects.filter(
        Q(inventory__lt=10) | Q(unit_price__lt=20)).order_by('-title', 'unit_price')
    queryset_5 = Product.objects.filter(
        Q(inventory__lt=10) & Q(unit_price__lt=20))
    queryset_6 = Product.objects.filter(
        Q(inventory__lt=10) | ~Q(unit_price__lt=20)).earliest('unit_price')
    queryset_7 = Product.objects.filter(inventory=F('unit_price'))
    queryset_8 = Product.objects.filter(
        unit_price__gt=F('collection__id')).latest('unit_price')
    queryset_9 = Product.objects.values(
        'id',
        'title',
        'collection__title'
    )
    queryset_9 = Product.objects.values_list(
        'id',
        'title',
        'collection__title'
    )

    # related_name and related_query_name
    queryset_10 = Product.objects.filter(
        orderitem__isnull=False).order_by('title').distinct()

    # distinct --> removes the duplicates
    queryset_11 = OrderItem.objects.values('order_id').distinct()
    queryset_12 = Product.objects.filter(id__in=queryset_11).order_by('title')

    return render(
        request,
        'hello.html',
        {
            'name': 'Hossein',
            'products': list(queryset_10)
        }
    )
