from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns=[
    path('register/', views.UserRegisterView.as_View(), name='user_register'),
]