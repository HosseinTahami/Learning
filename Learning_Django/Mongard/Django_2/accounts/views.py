from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, UserLoginForm
from .models import Relation


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

    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get('next', None)
        return super().setup(request, *args, **kwargs)

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
                if self.next:
                    return redirect(self.next)
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
        is_followed = Relation.objects.filter(
            follower=request.user, followee__id=user_id).exists()
        user = User.objects.get(id=user_id)
        # posts = Post.objects.filter(user__id=user_id)
        posts = user.posts.all()
        return render(request, 'accounts/profile.html', {'user': user, 'posts': posts, 'is_followed': is_followed})


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


class UserRelationView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        followee = User.objects.get(id=user_id)
        relation = Relation.objects.filter(
            follower=request.user, followee=followee)
        if relation.exists():
            relation.delete()
            messages.success(request, f'you unfollowed {followee}', 'danger')

        else:
            Relation.objects.create(follower=request.user, followee=followee)
            messages.success(
                request, f' you are following { followee }', 'success')

        return redirect('accounts:user_profile', followee.id)
