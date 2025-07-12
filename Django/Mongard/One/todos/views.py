from django.shortcuts import render
from . import models

def todos_list(request):
    todos = models.Todo.objects.all()
    return render(request, 'todos.html', {"todos":todos})