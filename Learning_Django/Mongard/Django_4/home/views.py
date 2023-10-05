from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView, status
from .models import Person, Car, Question, Answer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import PersonSerializer, CarSerializer, QuestionSerializer
from rest_framework import status
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

    
class QuestionListView(APIView):
    
    def get(self, request):
        questions = Question.objects.all() 
        questions_ser = QuestionSerializer(instance=questions, many=True)
        return Response(questions_ser.data, status=status.HTTP_200_OK)
    
class QuestionCreateView(APIView):
    def post(self, request):
        srz_data = QuestionSerializer(data=request.POST)
        if srz_data. is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):
    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response(
            {
                'messages':'Question Deleted Successfully'
            },
            status=status.HTTP_202_ACCEPTED
        )


class QuestionEditView(APIView):
    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        srz_question = QuestionSerializer(instance=question, data=request.POST, partial=True)
        if srz_question.is_valid():
            srz_question.save()
            return Response(srz_question.data, status=status.HTTP_200_OK)
        return Response(srz_question.errors, status=status.HTTP_406_NOT_ACCEPTABLE)