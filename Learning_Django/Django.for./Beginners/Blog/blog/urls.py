from django.urls import path, include
from .views import PostList, PostDetail

urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path("post/<int:pk>/", PostDetail.as_view(), name="post_detail"),
]