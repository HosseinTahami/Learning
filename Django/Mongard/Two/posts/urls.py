from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("search/", views.PostSearchView.as_view(), name="post_search"),
    path("create/", views.PostCreateView.as_view(), name="post_create"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
    path("<int:pk>/update/", views.PostUpdateView.as_view(), name="post_update"),
    path("<slug:post_slug>/", views.PostDetailView.as_view(), name="post_detail"),
    path("<int:post_pk>/like/", views.PostLikeView.as_view(), name="post_like"),
    path(
        "<int:post_pk>/comment/<int:comment_pk>/reply/",
        views.ReplyCommentView.as_view(),
        name="reply_comment",
    ),
    
]
