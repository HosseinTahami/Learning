from django.urls import path
from . import views

urlpatterns = [
    path("home/1/", views.home),
    path("home/2/", views.Home.as_view()),
    path("persons", views.PersonView.as_view()),
    path('first/<str:name>', views.First.as_view()),
    path('cars/', views.CarView.as_view()),
    path('questions/create/', views.QuestionCreateView.as_view()),
    path('questions/list/', views.QuestionListView.as_view()),
    path('questions/edit/<int:pk>/', views.QuestionEditView.as_view()),
    path('questions/delete/<int:pk>/', views.QuestionDeleteView.as_view())
]

# these urls called 'End-Point' 