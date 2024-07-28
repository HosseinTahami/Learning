from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from django.shortcuts import redirect
from django.contrib import messages
from django.views import View

from .models import Post
from . import forms


class PostListView(View):

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request, "posts/post_list.html", {"posts": posts})


class PostDetailView(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, slug=kwargs["post_slug"])
        return render(request, "posts/post_detail.html", {"post": post})


class PostDeleteView(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        if post.author.id == request.user.id:
            post.delete()
            messages.success(request, f"{post.title} Deleted Successfully.", "primary")
            return redirect("posts:post_list")
        messages.success(request, "This post belongs to someone else.", "warning")
        return redirect("pages:home")


class PostUpdateView(LoginRequiredMixin, View):

    form_class = forms.PostUpdateForm
    template_name = "posts/post_update.html"

    def setup(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(Post, pk=kwargs["pk"])
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        post = self.post_instance
        if post.author.id != request.user.id:
            messages.error(request, "This Post Does Not Belongs to you.")
            return redirect("pages:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        post = self.post_instance
        form = self.form_class(instance=post)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        post = self.post_instance
        form = self.form_class(request.POST, instance=post)
        if form.is_valid():
            updated_post = form.save(commit=False)
            updated_post.slug = slugify(form.cleaned_data["title"][:40])
            updated_post.save()
            messages.success(request, "Updated Successfully", "primary")
            return redirect(updated_post)
        return render(request, self.template_name, {"form": form})


class PostCreateView(LoginRequiredMixin, View):

    form_class = forms.PostCreateForm
    template_name = "posts/post_create.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form":form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(form.cleaned_data['title'][:40])
            new_post.author = request.user
            new_post.save()
            messages.success(request, f"{new_post.title} Created Successfully.", "primary")
            return redirect(new_post)
        return render(request, self.template_name, {"form":form})
        
