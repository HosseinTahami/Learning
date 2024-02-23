from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Todo
from .forms import TodoCreateForm, TodoUpdateForm


def home(request):
    all_todo = Todo.objects.all()
    return render(request, 'home.html', {'todos': all_todo})


def details(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {'todo': todo})


def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    messages.success(request, 'Todo deleted successfully!', 'danger')
    return redirect('home')


def create(request):

    if request.method == "POST":
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(
                title=cd['title'],
                body=cd['body'],
                created_at=cd['created_at']
            )
            messages.success(request, 'Todo Created Successfully !', 'success')
            return redirect('home')
    else:
        form = TodoCreateForm()
        return render(request, 'create.html', {'form': form})


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == "POST":
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo Updated Successfully !', 'primary')
            return redirect('home')
    else:
        form = TodoUpdateForm(instance=todo)
        return render(request, 'update.html', {'form': form})
