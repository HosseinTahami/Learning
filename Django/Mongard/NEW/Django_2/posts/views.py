from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post


class PostView(View):

    def get(self, request):
        posts = Post.objects.all()
        return render(request, "posts/posts_list.html", {"posts": posts})


class PostDetail(View):
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        return render(request, "posts/posts_detail.html", {"post": post})
