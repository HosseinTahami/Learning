from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("posts/", views.PostView.as_view(), name="posts_list"),
    path("posts/<int:pk>/<slug:post_slug>", views.PostDetail.as_view(), name="posts_detail"),
]
