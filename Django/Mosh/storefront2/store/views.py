from django.shortcuts import get_object_or_404
from django.http import HttpResponse

# Rest Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Inside Project Imports
from .models import Product, Collection
from .serializers import ProductSerializer, CollectionSerializer


@api_view(['GET', 'POST'])
def product_list(request):

    if request.method == 'GET':
        queryset = Product.objects.all()
        serializer = ProductSerializer(
            instance=queryset, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def product_detail(request, *args, **kwargs):
    product = get_object_or_404(Product, pk=kwargs['product_id'])
    if request.method == 'GET':
        serializer = ProductSerializer(
            instance=product, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ProductSerializer(
            product, data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        if product.orderitem_set.count() > 0:
            return Response(
                {
                    "error": "This Product Can not be deleted because it is associated with an orderitem..!"
                },
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def collection_detail(request, *args, **kwargs):
    collection = get_object_or_404(Collection, pk=kwargs['pk'])
    if request.method == 'GET':
        serializer = CollectionSerializer(instance=collection)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = CollectionSerializer(data=request.data)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def collection_list(request, *args, **kwargs):
    if request.method == 'POST':
        ...
    elif request.method == 'GET':
        ...
    elif request.method == 'DELETE':
        ...
