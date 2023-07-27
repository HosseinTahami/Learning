from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(
                cd['username'],
                cd['email'],
                cd['password']
            )
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form':form})

