# Django Imports

from django.shortcuts import render
from django.views import View


# Rest Framework Imports

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


@api_view(['GET', 'POST', 'PUT'])
def home(request):
    return Response({'name': 'Hossein'})


class HomeView(APIView):
    def get(self, request):
        return Response({'name': 'Ali'})
