from django.shortcuts import render
from django.http import HttpResponse

# Rest Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        return Response('OK')

    if request.method == 'POST':
        ...


@api_view(['GET', 'POST'])
def product_detail(request, *args, **kwargs):
    return Response(kwargs['product_id'])
