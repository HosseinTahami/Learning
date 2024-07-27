from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

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

        user = User.objects.get(pk=kwargs["pk"])
        return render(request, "accounts/profile.html", {"user": user})

    def post(self, request, *args, **kwargs): ...
