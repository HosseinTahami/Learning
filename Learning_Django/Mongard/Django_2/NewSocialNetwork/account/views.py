""" Django Imports """
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages

""" Projects Import """
from .forms import UserRegisterForm

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'account/register.html', {'form':form})

    def post(self, request):
        print("POST")
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(email=cd['email'], username=cd['username'], password=cd['password'])
            messages.success(request, 'Registration Completed', 'success')
            return redirect('home:home')