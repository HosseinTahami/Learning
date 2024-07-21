from django.urls import path

from . import views


urlpatterns = [
    path("", views.homepage_view, name="home"),
    path("todo/", views.todo_listview, name="todo_list"),
    path("todo/<int:pk>/", views.todo_detailview, name="todo_detail"),
    path("todo/<int:pk>/delete/", views.todo_deleteview, name="todo_delete"),
]
