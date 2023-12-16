""" Django Imports """
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages

""" Projects Import """
from .forms import UserRegisterForm

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
    ...