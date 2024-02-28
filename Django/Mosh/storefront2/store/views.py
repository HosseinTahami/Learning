from django.shortcuts import get_object_or_404
from django.http import HttpResponse

# Rest Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Inside Project Imports
from .models import Product
from .serializers import ProductSerializer, CollectionSerializer


@api_view(['GET', 'POST'])
def product_list(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(
        instance=queryset, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def product_detail(request, *args, **kwargs):
    try:
        product = get_object_or_404(Product, pk=kwargs['product_id'])
        serializer = ProductSerializer(instance=product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def collection_detail(request, *args, **kwargs):
    try:
        collection = get_object_or_404(Product, pk=kwargs['pk'])
        serializer = CollectionSerializer(instance=collection)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
