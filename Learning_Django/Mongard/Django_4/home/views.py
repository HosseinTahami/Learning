from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Person
from .serializers import PersonSerializer


@api_view(["GET", "POST", "PUT", "DELETE"])
def home(request):
    data = {
        "First_name": "Hossein",
        "Last_name": "Tahami",
        "age": 22,
    }
    # Response : take a dict and convert it to json
    return Response(data)


class Home(APIView):
    def get(self, request):
        name = request.query_params[
            "name"
        ]  # --> http://127.0.0.1:8000/home/2/?name=kevin
        return Response({"name": name})

    def post(self, request):
        name = request.data["name"]  # --> inside the body of url {'name' : 'kevin'}
        return Response({"name": name})


class PersonView(APIView):
    def get(self, request):
        persons = Person.objects.all()
        ser_per = PersonSerializer(instance=persons, many=True)
        return Response(data=ser_per.data)
