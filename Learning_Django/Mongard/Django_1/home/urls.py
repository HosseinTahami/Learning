from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:todo_id>/', views.details, name='detail'),
    path('', views.home, name='home'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('create/', views.create, name='create'),

]
