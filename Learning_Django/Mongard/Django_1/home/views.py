from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo
# Create your views here.


def home(request):
    all_todo = Todo.objects.all()
    return render(request, 'home.html', {'todos': all_todo})


def details(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {'todo': todo})


def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('home')
