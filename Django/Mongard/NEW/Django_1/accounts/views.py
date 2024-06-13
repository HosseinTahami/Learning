from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import UserRegistration, UserLoginFrom


def register(request):
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(
                cd['username'], cd['email'], cd['password'])
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.save()
            messages.success(request, 'Registration Completed !', 'success')
            return redirect('show_todos')
    if request.method == "GET":
        form = UserRegistration()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginFrom(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'login successfully !')
                return redirect('show_todos')
            messages.error(
                request, 'Username or Password incorrect !', 'danger')
    elif request.method == 'GET':
        form = UserLoginFrom()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'Logout Successfully !', 'success')
    return redirect('show_todos')
