# REST Framework Imports

from rest_framework import serializers


class UserRegisterSerializer(serializers.Serializer):

    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate_username(self, username):
        if username == 'admin':
            raise serializers.ValidationError("username can not be 'admin'..!")
        return username
