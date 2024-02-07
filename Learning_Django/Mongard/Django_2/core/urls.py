# Django imports
from django.urls import path

# Project imports
from . import views

urlpatterns = [
    path('', views.home, name='home')
]
