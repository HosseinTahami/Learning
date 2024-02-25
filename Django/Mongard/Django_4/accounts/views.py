# REST Framework Imports

from rest_framework.views import APIView
from rest_framework.response import Response

# Django Imports

from django.contrib.auth.models import User

# Inside Project Imports

from .serializers import UserRegisterSerializer


class UserRegisterView(APIView):

    def post(self, request, *args, **kwargs):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            vd = ser_data.validated_data
            User.objects.create_user(
                username=vd['username'],
                email=vd['email'],
                password=vd['password']
            )
            return Response(ser_data.data)
        return Response(ser_data.errors)
