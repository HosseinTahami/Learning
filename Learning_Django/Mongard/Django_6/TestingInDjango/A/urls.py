from django.urls import path
from .views import Home, About

app_name = "home"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("about/", About.as_view(), name="about"),
]