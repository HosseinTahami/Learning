from django.views import View
from django.shortcuts import render, get_object_or_404

from .models import Post


class PostListView(View):

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request, "posts/post_list.html", {"posts":posts})
    

class PostDetailView(View):

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, slug=kwargs["post_slug"])
        return render(request, "posts/post_detail.html", {"post":post})