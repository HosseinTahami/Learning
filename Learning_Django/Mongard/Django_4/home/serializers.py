from rest_framework import serializers
from .models import Car, Question, Answer
from .custom_related_fields import UsernameEmailRelationalField
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
    #user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    #user = serializers.StringRelatedField(read_only=True) # --> shows whats in the __str__ of model
    user = UsernameEmailRelationalField(read_only=True)
    class Meta:
        model = Question
        fields = '__all__'
    
    def get_answers(self, obj):
        
        # answer in the below line is the related_name we chose ourselves in the models.py
        result = obj.answers.all()
        return AnswerSerializer(instance=result, many=True).data