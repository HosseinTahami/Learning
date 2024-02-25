# REST Framework Imports

from rest_framework import serializers

''' First Type of Validation in DRF
    Put the name of function inside a list
    and send it in the specific field as an
    Argument named 'validator' '''


def clean_email(email):
    if 'admin' in email:
        raise serializers.ValidationError("'admin' can not be in email..!")


class UserRegisterSerializer(serializers.Serializer):

    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True, validators=[clean_email])
    password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    def validate_username(self, username):
        if username == 'admin':
            raise serializers.ValidationError("username can not be 'admin'..!")
        return username
