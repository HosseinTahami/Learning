from rest_framework import serializers
from .models import Car, Question, Answer

class PersonSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    age = serializers.IntegerField()

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Answer
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = '__all__'