from django.urls import path
from . import views

urlpatterns = [
    path('', views.todos_list),
    path('detail/<int:todo_id>/', views.todo_detail, name='todo_detail'),
]