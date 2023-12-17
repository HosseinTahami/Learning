# Django imports
from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import PostUpdateForm
from django.utils.text import slugify

class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'home/index.html', {'posts':posts})
    
    def post(self, request):
        return render(request, 'home/index.html')

class PostDetailView(View):
    def get(self, request, post_id, post_slug):
        post = Post.objects.get(pk=post_id, slug=post_slug)
        return render(request, 'home/detail.html', {'post': post})

class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        if request.user.id == post.user.id:
            post.delete()
            messages.success(request, 'Post Deleted Successfully !', 'warning')
        else:
            messages.error(request, 'You Cant delete this Post !', 'danger')
        return redirect('home:home')

class PostUpdateView(LoginRequiredMixin, View):

    form_class = PostUpdateForm
    template_name = 'home/update.html'

    def setup(self, request: HttpRequest, *args: Any, **kwargs: Any) -> None:
        self.post_instance = Post.objects.get(pk=kwargs['post_id'])
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        post = self.post_instance
        if request.user.id != post.user.id:
            messages.error(request, 'You Cant Update this Post', 'danger')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, post_id):
        post = self.post_instance
        form = self.form_class(instance=post)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request, post_id):
        post = self.post_instance
        form = self.form_class(request.POST, instance=post)
        if form.is_valid:
            new_form = form.save(commit=False)
            new_form.slug = slugify(new_form.body[:30])
            new_form.save()
            messages.success(request, 'Post Updated Successfully !', 'success')
            return redirect('home:post_detail', post.id, post.slug)