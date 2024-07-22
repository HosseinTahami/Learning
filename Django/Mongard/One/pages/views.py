from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Todo
from . import forms


def homepage_view(request):
    return render(request=request, template_name="pages/home.html")


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
    messages.success(
        request=request,
        message=f"{todo.title} deleted successfully.",
        extra_tags="warning",
    )
    return redirect("todo_list")


def todo_createview(request):

    if request.method == "POST":

        form = forms.TodoCreateForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            Todo.objects.create(
                title=clean_data["title"],
                body=clean_data["body"],
            )

            messages.success(
                request=request,
                message=f"{clean_data['title']} created successfully.",
                extra_tags="success",
            )

            return redirect("todo_list")

    if request.method == "GET":
        form = forms.TodoCreateForm()

    return render(
        request=request,
        template_name="pages/todo_create.html",
        context={"form": form},
    )


def todo_updateview(request, pk):

    todo = Todo.objects.get(pk=pk)
    if request.method == "POST":
        form = forms.TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request=request, message=f"{form.cleaned_data['title']} Updated Successfully.", extra_tags="info")
            return redirect(todo)
        
    if request.method == "GET":

        form = forms.TodoUpdateForm(instance=todo)
    return render(
            request=request,
            template_name="pages/todo_update.html",
            context={"form": form},
        )
