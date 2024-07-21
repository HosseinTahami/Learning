from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Todo


def homepage_view(request):
    # person = {"name":"admin"}
    person = {"name": "Hossein", "age": 24, "job": "Developer"}
    return render(request=request, template_name="pages/home.html", context=person)


def todo_listview(request):
    todos = Todo.objects.all()
    return render(
        request=request, template_name="pages/todo_list.html", context={"todos": todos}
    )


def todo_detailview(request, pk):
    todo = Todo.objects.get(pk=pk)
    return render(
        request=request, template_name="pages/todo_detail.html", context={"todo": todo}
    )

def todo_deleteview(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    messages.success(request=request, message=f"{todo.title} deleted successfully.", extra_tags="danger")
    return redirect("todo_list")