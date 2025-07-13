from django.shortcuts import render
from . import models

def todos_list(request):
    todos = models.Todo.objects.all()
    return render(request, 'todos.html', {"todos":todos})

def todo_detail(request, todo_id):
    todo = models.Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {"todo":todo})