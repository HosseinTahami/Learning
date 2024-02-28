# Rest Framework Imports

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

# Inside Project Imports
from .models import Person
from .serializers import PersonSerializer


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

        first_name = kwargs['first_name']  # .../Kevin/
        # ?last_name=...
        last_name = request.GET['last_name'] or request.query_params['last_name']

        return Response(
            {
                'f_name': first_name,
                'l_name': last_name
            }
        )


class PersonView(APIView):
    ''' Inside Headers:
        Authorization: Token (...)
    '''
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        person = Person.objects.all()
        ser_data = PersonSerializer(instance=person, many=True)
        return Response(data=ser_data.data)
