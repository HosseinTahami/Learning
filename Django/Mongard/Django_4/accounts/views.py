# Django Imports
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import viewsets

# Inside Project Imports
from .serializers import UserRegisterSerializer, UserSerializer

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
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ViewSet):
    
    permission_classes = [IsAuthenticated,]
    queryset = User.objects.all()
    
    def list(self, request):
        srz_data = UserSerializer(instance=self.queryset, many=True)
        return Response(data=srz_data.data)
        
    
    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        srz_data = UserSerializer(instance=user)
        return Response(data=srz_data.data)
    
    def destroy(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        if user != request.user:
            return Response(
                {
                    'message':'You are not the owner of this user'
                }
            )
        user.is_active = False
        user.save()
        return Response(
            {
                'message':'User Deactivated Successfully'
            }
        )
    
    def partial_update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        if user != request.user:
            return Response(
                {
                    'message':'You are not the owner of this user'
                }
            )
        srz_data = UserSerializer(instance=user, data=request.POST, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
    