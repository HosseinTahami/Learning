# Django imports
from django.urls import path

# Project imports
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home')
]
