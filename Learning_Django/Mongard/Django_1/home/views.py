from django.shortcuts import render
from django.http import HttpResponse

from .models import Todo
# Create your views here.


def home(request):
    all_todo = Todo.objects.all()
    return render(request, 'home.html', {'todos': all_todo})


def say_hello(request):
    person = {
        'name': 'admin'
    }
    return render(request, 'hello.html', person)
