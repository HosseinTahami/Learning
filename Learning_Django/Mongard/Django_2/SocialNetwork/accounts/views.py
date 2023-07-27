from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages

class UserRegister(View):
    form_class = UserRegisterForm
    def get(self, request):
        form = self.form_class()
        return render(request,
                      'accounts/register.html',
                      {'form': form}
                    )
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(
                cd['username'],
                cd['email'],
                cd['password']
            )
            messages.success(
                request,
                'Account created successfully',
                'success'
                )
            return redirect('home:home')
