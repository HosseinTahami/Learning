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
    
    answers = serializers.SerializerMethodField()
    class Meta:
        model = Question
        fields = '__all__'
    
    def get_answers(self, obj):
        
        # answer in the below line is the related_name we chose ourselves in the models.py
        result = obj.answers.all()
        return AnswerSerializer(instance=result, many=True).data