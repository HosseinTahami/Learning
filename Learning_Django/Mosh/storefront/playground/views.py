from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, Order, OrderItem, Customer
from django.db.models import Q, F, Value, Func
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max, Min, Avg, Sum


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

    # values --> return dictionary
    queryset_13 = Product.objects.values('id', 'collection__title')

    # values_list --> return tuple
    queryset_14 = Product.objects.values_list('id', 'title')

    # defer() and only() are opposite of each other !
    queryset_15 = Product.objects.only('id', 'title')

    queryset_16 = Product.objects.defer('description')

    # select_related will preload what we want but for single objects !
    # prefetch_related will preload what we want but for multi objects !
    # Product have only one collection but multiple promotions !
    queryset_17 = Product.objects.select_related('collection').all()
    queryset_18 = Product.objects.prefetch_related('promotions').all()
    queryset_19 = Product.objects.prefetch_related(
        'promotions').select_related('collection').all()
    queryset_20 = Order.objects.select_related(
        'customer').prefetch_related('orderitem_set__product ').order_by('-placed_at')[:5]

    # {'id__count':500}
    queryset_21 = Order.objects.aggregate(Count('id'))

    # {'count':500, 'min_price':2.0}
    queryset_22 = Order.objects.aggregate(
        count=Count('id'), min_price=Min('unit_price'))

    queryset_23 = Order.objects.aggregate(count=Count('id'))

    queryset_24 = OrderItem.objects.filter(
        product__id=1).aggregate(total_sold=Sum('quantity'))

    queryset_25 = Product.objects.annotate(new_id=F(id)+10)

    queryset_26 = Product.objects.annotate(is_new=Value(True))

    # CONCATENATING
    queryset_27 = Product.objects.annotate(full_name=Func(
        F('first_name'), Value(' '), F('last_name'), function='CONCAT'))

    queryset_28 = Customer.objects.annotate(full_name=Concat(
        'first_name', Value(' '), 'last_name')
    )

    return render(
        request,
        'hello.html',
        {
            'name': 'Hossein',
            'orders': list(queryset_20)
        }
    )
