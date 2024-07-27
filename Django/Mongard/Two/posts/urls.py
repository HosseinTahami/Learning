from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("<slug:post_slug>/", views.PostDetailView.as_view(), name="post_detail"),
]
