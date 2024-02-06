from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')


def say_hello(request):
    person = {
        'name': 'admin'
    }
    return render(request, 'hello.html', person)
