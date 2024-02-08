# Django imports
from django.urls import path

# Project imports
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('post/<int:post_id>/<slug:post_slug>/',
         views.PostDetailView.as_view(), name='post_detail'),
    path('post/delete/<int:post_id>/',
         views.PostDeleteView.as_view(), name='post_delete'),
    path('post/update/<int:post_id>/',
         views.PostUpdateView.as_view(), name='post_update'),
    path('post/create/',
         views.PostCreateView.as_view(), name='post_create'),
    path('reply/<int:post_id>/<int:comment_id>/',
         views.ReplyCommentView.as_view(), name='comment_reply'),

]
