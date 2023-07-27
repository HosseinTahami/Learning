from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_user = User.objects.create_user(
                cd['username'],
                cd['email'],
                cd['password']
            )
            new_user.first_name = cd['first_name']
            new_user.last_name = cd['last_name']
            new_user.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form':form})


def user_login(request):
    if request.method == 'POST':
        pass
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form':form})
    