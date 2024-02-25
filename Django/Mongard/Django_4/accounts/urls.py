# Django Imports

from django.urls import path

# Inside Project Imports

from . import views


app_name = 'accounts'

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
]
