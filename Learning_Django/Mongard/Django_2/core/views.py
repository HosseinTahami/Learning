from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import PostCreateUpdateForm
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


class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        if post.user.id == request.user.id:
            post.delete()
            messages.success(request, 'Post Deleted Successfully', 'danger')
        else:
            messages.error(
                request, 'This Post Do not Belong To You', 'warning')
        return redirect('core:home')


class PostUpdateView(LoginRequiredMixin, View):
    template_name = 'core/update.html'
    form_class = PostCreateUpdateForm

    def setup(self, request, *args, **kwargs):
        self.post_instance = Post.objects.get(pk=kwargs['post_id'])
        super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        post = self.post_instance
        if not post.user.id == request.user.id:
            messages.error(
                request, 'This Post do not belong to you', 'warning')
            return redirect('core:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, post_id):
        post = self.post_instance
        form = self.form_class(instance=post)
        return render(request, self.template_name, {'form': form})

    def post(self, request, post_id):
        post = self.post_instance
        form = self.form_class(request.POST, instance=post)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(form.cleaned_data['body'][:30])
            new_post.save()
            messages.success(request, 'Post Updated Successfully !', 'success')
            return redirect('core:post_detail', post.id, post.slug)


class PostCreateView(LoginRequiredMixin, View):

    template_name = 'core/create.html'
    form_class = PostCreateUpdateForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(new_post.body[:30])
            new_post.user = request.user
            new_post.save()
            messages.success(request, 'Post Created', 'success')
            return redirect('core:home')
