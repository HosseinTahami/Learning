# REST Framework Imports

from rest_framework.authtoken.views import ObtainAuthToken

# Django Imports

from django.urls import path

# Inside Project Imports

from . import views


app_name = 'accounts'

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('registers/', views.OtherUserRegisterView.as_view(),
         name='other_user_register'),
    path('api-token-auth/', ObtainAuthToken.as_view()),
]
