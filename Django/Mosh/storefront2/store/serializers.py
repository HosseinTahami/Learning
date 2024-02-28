from decimal import Decimal

# REST Framework Imports
from rest_framework import serializers

# Inside Project Imports
from .models import Product, Collection


# class CollectionSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']


# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(
#         max_digits=6, decimal_places=2, source='unit_price')
#     price_with_tax = serializers.SerializerMethodField(
#         method_name='calculate_tax')
#     '''Primary Key Related Field'''
#     # collection_id = serializers.PrimaryKeyRelatedField(
#     #     queryset=Collection.objects.all()
#     # )
#     '''String Related Field'''
#     # collection = serializers.StringRelatedField()
#     '''Nested Object'''
#     # collection = CollectionSerializer()
#     '''Hyper Link Related Field'''
#     collection = serializers.HyperlinkedRelatedField(
#         queryset=Collection.objects.all(), view_name='collection_detail')

#     def calculate_tax(self, product: Product):
#         return product.unit_price * Decimal(1.1)
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug',
                  'inventory', 'collection', 'price', 'price_with_tax']
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(), view_name='collection_detail')
    price = serializers.DecimalField(
        decimal_places=2, max_digits=6, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
