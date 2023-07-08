from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def say_hello():
    return HttpRequest(" Hello MFs!")