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

    def post(self, request):
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        return Response(
            {
                'f_name': first_name,
                'l_name': last_name
            }
        )


class AnotherHomeView(APIView):

    def get(self, request, *args, **kwargs):

        first_name = kwargs['first_name']
        last_name = request.GET['last_name'] or request.query_params['last_name']

        return Response(
            {
                'f_name': first_name,
                'l_name': last_name
            }
        )
