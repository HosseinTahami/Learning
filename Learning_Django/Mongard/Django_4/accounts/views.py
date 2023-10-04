from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer


class UserRegister(APIView):
    def post(self, request):
        """
        The Reason we user Serializer(instance=...) & Serializer(data=...)
        is <instance> argument is used when you read data from db and want to convert it
        but <data> argument is used when we get them from user and we should validate them. 
        """
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            # vd = ser_data.validated_data
            # User.objects.create_user(
            #     username=vd["username"], email=vd["email"], password=vd["password"]
            # )
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data)
        else:
            return Response(ser_data.errors)
