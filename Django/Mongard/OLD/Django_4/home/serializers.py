# Rest Framework Imports

from rest_framework import serializers


# Inside Project Imports

from . import models


class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    email = serializers.EmailField()
    age = serializers.IntegerField()
