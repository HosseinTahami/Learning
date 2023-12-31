from rest_framework import serializers
from django.contrib.auth.models import User

# Validator
def clean_email(value):
    if "admin" in value:
        raise serializers.ValidationError("admin word should not be in email")


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        
        model = User
        fields = ("username", "password", "email", "confirm_password")
        #excludes = ("id", "...")
        
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"validators": (clean_email,)},
        }
        
        # OverWrite Create Method
    def create(self, validated_data):
        del validated_data["confirm_password"]
        # Python Function Argument Unpacking --> * / **
        return User.objects.create_user(**validated_data)


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


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'