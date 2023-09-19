from django.urls import path
from . import views

urlpatterns = [
    path("home/1/", views.home),
    path("home/2/", views.Home.as_view()),
    path("persons", views.PersonView.as_view()),
]