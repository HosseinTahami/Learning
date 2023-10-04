from rest_framework import serializers
from django.contrib.auth.models import User

# Validator
def clean_email(value):
    if "admin" in value:
        raise serializers.ValidationError("admin word should not be in email")


"""
class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True, validators=[clean_email])
    password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    def validate_username(self, value):
        if value == "admin":
            raise serializers.ValidationError("username can not be 'admin'")

        return value

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("passwords must match")
        return data
"""


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ("username", "password", "email", "confirm_password")
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"validators": (clean_email,)},
        }

        # Field Level Validation
        
        def validate_username(self, value):
            if value == "admin":
                raise serializers.ValidationError("username can not be 'admin'")

            return value
        
        
        # Object Level Validation --> you have to overwrite the validate method
        def validate(self, data):
            if data["password"] != data["confirm_password"]:
                raise serializers.ValidationError("passwords must match")
            return data
