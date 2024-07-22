from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from . import forms


def user_register(request):

    if request.method == "POST":

        form = forms.UserRegistrationForm(request.POST)

        if form.is_valid():

            clean_data = form.cleaned_data
            user = User.objects.create_user(
                username=clean_data["username"],
                email=clean_data["email"],
                password=clean_data["password"],
            )
            user.first_name = clean_data["first_name"]
            user.last_name = clean_data["last_name"]
            user.save()
            messages.success(
                request=request,
                message=f"Created account for {clean_data['username']}.",
            )

            return redirect("home")

    if request.method == "GET":

        form = forms.UserRegistrationForm()

    return render(
        request=request,
        template_name="accounts/user_registration.html",
        context={"form": form},
    )


def user_login(request):

    if request.method == "POST":
        form = forms.UserLoginForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data

        user = authenticate(
            request=request,
            username=clean_data["username"],
            password=clean_data["password"],
        )

        if user is not None:
            login(request, user)
            messages.success(
                request, f"{user.username} Logged In Successfully.", "primary"
            )
            return redirect("home")

        messages.error(request, "Username or Password is Wrong", "danger")

    if request.method == "GET":
        form = forms.UserLoginForm()

    return render(request, "accounts/user_login.html", {"form": form})


def user_logout(request):
    logout(request)
    messages.success(request, "logged out successfully", "warning")
    return redirect("home")
