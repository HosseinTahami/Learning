""" Django Imports """
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

""" Projects Import """
from .forms import (
    UserRegisterForm,
    UserLoginForm,
)

class UserRegisterView(View):
    form_class = UserRegisterForm
    template_name = 'account/register.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(
                username=cd['username'],
                email=cd['email'],
                password=cd['confirm_password']
            )
            messages.success(request, 'Registration Completed', 'success')
            return redirect('home:home')
        return render(request, self.template_name, {'form':form})

class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'account/login.html'
    
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form} )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], password = cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request,'Login Successfully', 'success')
                return redirect('home:home')
            messages.error(request,'Login Failed', 'danger')
            return render(request, self.template_name, {'form':form} )

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Logout Successfully', 'success')
        return redirect('home:home')