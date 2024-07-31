from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.utils.text import slugify
from django.shortcuts import redirect
from django.contrib import messages
from django.views import View

from .models import Post, Comment, Like
from . import forms


class PostListView(View):

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request, "posts/post_list.html", {"posts": posts})


class PostDetailView(LoginRequiredMixin,View):

    form_class = forms.CommentCreateForm
    form_class_reply = forms.CommentReplyForm

    def setup(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(Post, slug=kwargs["post_slug"])
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):

        form = self.form_class()
        reply_form = self.form_class_reply()
        post = self.post_instance
        comments = post.post_comments.filter(is_reply=False)
        like = Like.objects.filter(post=post, liker=request.user).exists()
        return render(
            request,
            "posts/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "form": form,
                "reply_form": reply_form,
                "like":like
            },
        )

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        post = self.post_instance
        if form.is_valid():
            comment = form.save(commit=False)
            comment.commenter = request.user
            comment.post = post
            comment.save()
            messages.success(request, "Your Comment submitted Successfully.")
            return redirect(post)


class PostDeleteView(LoginRequiredMixin, View):

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
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(form.cleaned_data["title"][:40])
            new_post.author = request.user
            new_post.save()
            messages.success(
                request, f"{new_post.title} Created Successfully.", "primary"
            )
            return redirect(new_post)
        return render(request, self.template_name, {"form": form})


class ReplyCommentView(LoginRequiredMixin, View):

    form_class = forms.CommentReplyForm

    def post(self, request, *args, **kwargs):

        post = get_object_or_404(Post, pk=kwargs["post_pk"])
        comment = get_object_or_404(Comment, pk=kwargs["comment_pk"])
        form = self.form_class(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.post = post
            reply.is_reply = True
            reply.commenter = request.user
            reply.reply = comment
            reply.save()
            messages.success(
                request, "Your reply was submitted successfully.", "primary"
            )
        return redirect(post)


class PostLikeView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["post_pk"])
        like = Like.objects.filter(post=post, liker=request.user)
        if like.exists():
            like.delete()
            messages.success(request, "you removed your like.", "success")
        else:
            Like.objects.create(liker=request.user, post=post)
            messages.success(request, "you liked this post.", "success")

        return redirect(post)

class PostSearchView(View):
    def get(self, request, *args, **kwargs):
        search_item = request.GET.get("q")
        posts = Post.objects.filter(
            title__icontains=search_item
        )
        return render(request, "posts/post_search.html", {"posts":posts})