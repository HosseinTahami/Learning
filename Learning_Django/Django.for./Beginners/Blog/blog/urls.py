from django.urls import path, include
from .views import PostList

urlpatterns = [
    path("", PostList.as_view(), name="home")
]