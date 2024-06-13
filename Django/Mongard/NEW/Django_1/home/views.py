from django.shortcuts import render
from .models import Todo


def show_todos(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})


def show_todo_detail(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    return render(request, 'todo_detail.html', {'todo': todo})
