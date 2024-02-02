from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models.aggregates import Count
from django.http.request import HttpRequest
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return f"Low - {product.inventory}"
        elif product.inventory > 50:
            return f"High - {product.inventory}"
        return f"OK - {product.inventory}"


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_count']

    @admin.display(ordering='product_count')
    def product_count(self, collection):
        return collection.product_count

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(
            product_count=Count('product')
        )


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer_name']
    list_select_related = ['customer']

    def customer_name(self, order):
        return f'{order.customer.first_name} {order.customer.last_name}'

# admin.site.register(models.Product, ProductAdmin)
# admin.site.register(models.Collection, CollectionAdmin)
