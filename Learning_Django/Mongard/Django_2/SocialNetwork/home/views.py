from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Post
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostUpdateForm
from django.utils.text import slugify


class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, "home/index.html", {"posts": posts})


class PostDetailView(View):
    def get(self, request, post_id, post_slug):
        post = Post.objects.get(id=post_id, slug=post_slug)
        return render(request, "home/post.html", {"post": post})


class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        if request.user.id == post.user.id:
            post.delete()
            messages.success(request, "Post Deleted Successfully !", "success")
        else:
            messages.error(request, "This post Does not belong to you!", "danger")
        return redirect("home:home")


class PostUpdateView(LoginRequiredMixin, View):
    form_class = PostUpdateForm

    def setup(self, request, *args, **kwargs):
        self.post_instance = Post.objects.get(id=kwargs["post_id"])
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        post = self.post_instance
        if not post.user.id == request.user.id:
            messages.error(request, "Not your post to update", "danger")
            return redirect("home:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, post_id):
        post = self.post_instance
        form = self.form_class(instance=post)
        return render(request, "home/post_update.html", {"form": form})

    def post(self, request, post_id):
        post = self.post_instance
        form = self.form_class(request.POST, instance=post)
        if form.is_valid:
            new_post = form.save(commit=False)
            new_post.slug = slugify(form.cleaned_data["title"])
            new_post.save()
            messages.success(request, "Post Updated Successfully", "success")
            return redirect("home:home")
