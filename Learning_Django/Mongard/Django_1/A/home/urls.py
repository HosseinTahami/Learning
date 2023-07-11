from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home),
    path('hello/', views.say_hello),
    path('bye/', views.say_bye),
    path('Todo/',views.read_Todo)
    
]