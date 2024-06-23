from django.shortcuts import render, redirect
from django.views import View
from .models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from . import forms
from posts.models import Post

class UserRegistrationView(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = forms.RegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(
                username=cd['username'], email=cd['email'], password=cd['password'])
            messages.success(request, 'Registration Completed !', 'success')
            return redirect('home:home')
        return render(request, 'accounts/register.html', {'form': form})


class UserLoginView(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = forms.LoginForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                messages.success(
                    request, f"Logged in as {cd['username']} !", 'primary')
                return redirect('home:home')
            messages.error(request, 'Wrong Username or Password !', 'danger')
        return render(request, 'accounts/login.html', {'form': form})


class UserLogoutView(LoginRequiredMixin, View):

    def get(self, request):
        logout(request)
        messages.success(request, 'Logged Out of your account !', 'warning')
        return redirect('accounts:login')


class UserProfileView(LoginRequiredMixin, View):

    def get(self, request, user_username, *args, **kwargs):

        try:
            user = User.objects.get(username=user_username)
            posts = Post.objects.filter(user=user)
            return render(request, 'accounts/profile.html', {'user': user, 'posts':posts})

        except:
            messages.error(request, 'This User Does Not Exist !', 'warning')
            return redirect('accounts:profile', user_username=request.user.username)
