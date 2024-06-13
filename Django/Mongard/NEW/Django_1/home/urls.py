from django.urls import path

from . import views

urlpatterns = [
    path('todos/', views.show_todos, name='show_todos'),
    path('todos/<int:todo_id>', views.show_todo_detail, name='todo_detail'),
    path('todos/delete/<int:todo_id>', views.delete_todo, name='todo_delete'),
    path('todos/create/', views.create_todo, name='create_todo'),
    path('todos/update/<int:todo_id>', views.update_todo, name='update_todo'),
]
