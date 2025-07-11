from django.urls import path

from . import views


urlpatterns = [
    path("", views.homepage_view, name="home"),
    path("todo/", views.todo_listview, name="todo_list"),
    path("todo/create/", views.todo_createview, name="todo_create"),
    path("todo/<int:pk>/", views.todo_detailview, name="todo_detail"),
    path("todo/<int:pk>/delete/", views.todo_deleteview, name="todo_delete"),
    path("todo/<int:pk>/update/", views.todo_updateview, name="todo_update"),

]
