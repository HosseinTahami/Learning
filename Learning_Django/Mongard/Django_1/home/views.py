from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Todo
from .forms import TodoCreateForm


def home(request):
    all_todo = Todo.objects.all()
    return render(request, 'home.html', {'todos': all_todo})


def details(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {'todo': todo})


def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    messages.success(request, 'Todo deleted successfully!', 'success')
    return redirect('home')


def create(request):
    form = TodoCreateForm()
    return render(request, 'create.html', {'form': form})
