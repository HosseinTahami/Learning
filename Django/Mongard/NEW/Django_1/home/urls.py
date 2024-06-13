from django.urls import path

from . import views

urlpatterns = [
    path('todos/', views.show_todos, name='show_todos'),
    path('todos/<int:todo_id>', views.show_todo_detail, name='todo_detail'),
]
