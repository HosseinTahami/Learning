from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView, status
from .models import Person, Car
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import PersonSerializer, CarSerializer

@api_view(["GET", "POST", "PUT", "DELETE"])
def home(request):
    data = {
        "First_name": "Hossein",
        "Last_name": "Tahami",
        "age": 22,
    }
    # Response : take a dict and convert it to json
    return Response(data, status=status.HTTP_200_OK)


class Home(APIView):
    def get(self, request):
        
        # name = request.GET['name']
        name = request.query_params[
            "name"
        ]  # --> http://127.0.0.1:8000/home/2/?name=kevin
        return Response({"name": name})

    def post(self, request):
        info = request.data # --> inside the body of url {'name' : 'kevin'}
        # name = request.data['name']
        # age = request.data['age']
        return Response(info)


class First(APIView):
    def get(self, request, name):
        return Response({'name':name})

class PersonView(APIView):
    
    permission_classes = [IsAdminUser,]
    
    def get(self, request):
        persons = Person.objects.all()
        ser_per = PersonSerializer(instance=persons, many=True)
        return Response(data=ser_per.data)

class CarView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        ser_data = CarSerializer(instance=cars, many=True)
        return Response(data=ser_data.data)