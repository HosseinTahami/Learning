from django.shortcuts import render
from django.views import View
from .models import Post


class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'core/home.html', {'posts': posts})

    def post(self, request):
        return render(request, 'core/home.html')


class PostDetailView(View):
    def get(self, request, post_id, post_slug):
        post = Post.objects.get(id=post_id)
        return render(request, 'core/detail.html', {'post': post})
