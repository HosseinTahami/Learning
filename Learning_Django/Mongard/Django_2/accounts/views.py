from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import Post
from django.urls import reverse_lazy


class UserRegisterView(View):
    from_class = UserRegistrationForm
    template_name = 'accounts/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.from_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.from_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            User.objects.create_user(
                cd['username'], cd['email'], cd['password'])
            messages.success(
                request, 'User Registered Successfully !', 'success')
            return redirect('core:home')
        return render(request, self.template_name, {'form': form})


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['authenticator'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged In Successfully!', 'success')
                return redirect('core:home')
            messages.error(request, 'Password or Username is Wrong', 'danger')
        return render(request, self.template_name, {'form': form})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Logged Out Successfully', 'warning')
        return redirect('core:home')


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        posts = Post.objects.filter(user__id=user_id)
        return render(request, 'accounts/profile.html', {'user': user, 'posts': posts})


class UserPasswordResetView(PasswordResetView):
    template_name = 'accounts/password/password_reset_form.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    email_template_name = 'accounts/password/password_reset_email.html'


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password/password_reset_done.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password/password_reset_complete.html'