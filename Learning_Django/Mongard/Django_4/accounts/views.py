from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer


class UserRegister(APIView):
    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            vd = ser_data.validated_data
            User.objects.create_user(
                username=vd["username"], email=vd["email"], password=vd["password"]
            )
            return Response(ser_data.data)
        else:
            return Response(ser_data.errors)