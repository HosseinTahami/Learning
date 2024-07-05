from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CreateTodoForm, UpdateTodoForm
from .models import Todo


def show_todos(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})


def show_todo_detail(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    return render(request, 'todo_detail.html', {'todo': todo})


def delete_todo(request, todo_id):
    title = Todo.objects.get(pk=todo_id).title
    Todo.objects.get(pk=todo_id).delete()
    messages.success(request, f'Todo {title} deleted', 'success')
    return redirect('show_todos')


def update_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    if request.method == 'POST':
        form = UpdateTodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo Updated Successfully !', 'info')
            return redirect('show_todos')
    elif request.method == 'GET':
        form = UpdateTodoForm(instance=todo)
    return render(request, 'update.html', {'form': form})


def create_todo(request):

    if request.method == 'GET':
        form = CreateTodoForm()

    if request.method == 'POST':
        form = CreateTodoForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'], body=cd['body'])
            messages.success(request, 'Todo Created Successfully !', 'warning')
            return redirect('show_todos')
    return render(request, 'create_todo.html', {'form': form})