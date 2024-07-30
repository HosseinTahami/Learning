from django.contrib.auth import get_user_model, login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View

from .models import Relation
from . import forms

User = get_user_model()


class UserRegisterView(View):

    form_class = forms.UserRegisterForm
    template_name = "accounts/register.html"

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect("pages:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):

        form = self.form_class()
        return render(
            request=request, template_name=self.template_name, context={"form": form}
        )

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)

        if form.is_valid():

            clean_data = form.cleaned_data
            User.objects.create_user(
                username=clean_data["username"],
                email=clean_data["email"],
                password=clean_data["password"],
            )

            messages.success(
                request=request, message=f"{clean_data['email']} is registered."
            )

            return redirect("pages:home")

        return render(
            request=request, template_name=self.template_name, context={"form": form}
        )


class UserLoginView(View):

    form_class = forms.UserLoginForm
    template_name = "accounts/login.html"

    def setup(self, request, *args, **kwargs):
        self.next_url = request.GET.get("next")
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect("pages:home")
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            user = authenticate(
                request,
                username=clean_data["username"],
                password=clean_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(
                    request, f"{clean_data['username']} Logged In Successfully."
                )
                if self.next_url:
                    return redirect(self.next_url)
                return redirect("pages:home")
        messages.error(request, "Wrong Credentials try again.", extra_tags="danger")
        return render(request, self.template_name, {"form": form})

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(
            request=request, template_name=self.template_name, context={"form": form}
        )


class UserLogoutView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        user = request.user
        logout(request)
        messages.success(
            request, f"{user.username} Logged Out Successfully.", "warning"
        )
        return redirect("pages:home")

    def get(self, request, *args, **kwargs):
        return render(request, "accounts/logout.html")


class UserProfileView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        
        user = get_object_or_404(User, pk=kwargs["pk"])
        relation_status = Relation.objects.filter(follower=request.user, following=user.pk).exists()
        return render(request, "accounts/profile.html", {"user": user, "relation_status":relation_status})

    def post(self, request, *args, **kwargs): ...


class UserPasswordResetView(auth_views.PasswordResetView):
    template_name = "accounts/password/password_reset_form.html"
    email_template_name = "accounts/password/password_reset_email.html"
    success_url = reverse_lazy("accounts:password_reset_done")


class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
    # To show an page that email was sent
    template_name = "accounts/password/password_reset_done.html"


class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = "accounts/password/password_reset_confirm.html"
    success_url = reverse_lazy("accounts:password_reset_complete")


class UserPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = "accounts/password/password_reset_complete.html"
    success_url = reverse_lazy("accounts:profile")


class FollowView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        user = get_object_or_404(User, pk=kwargs["pk"])
        relation = Relation.objects.filter(follower=request.user, following=user).exists()
        if relation:
            messages.warning(request, f"you already follow {user.username}.", "warning")
        else:
            Relation.objects.create(
                follower = request.user, following=user
            )
            messages.success(request, f"you start following {user.username}.", "warning")
        return redirect("accounts:profile", user.pk)
    
class UnfollowView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs["pk"])
        relation = Relation.objects.filter(follower=request.user, following=user)
        if not relation.exists():
            messages.warning(request, f"you are not following {user.username}.", "warning")
        else:
            relation.delete()
            messages.success(request, f"You unfollowed {user.username}.", "warning")
        return redirect("accounts:profile", user.pk)