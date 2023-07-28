from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm, UserLoginForm, UserLogoutForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

class UserRegister(View):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    def get(self, request):
        form = self.form_class()
        return render(request,
                      self.template_name,
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
        return render(
            request,
            self.template_name,
            {'form':form}
            )


class UserLoginView(View):
    form_class=UserLoginForm
    template_name = 'accounts/login.html'
    def get(self, request):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {'form': form}
            )
    
    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username = cd['username'],
                password = cd['password']
            )
            if user is not None:
                login(request, user)
                messages.success(
                    request,
                    'Logged in successfully',
                    'success'
                )
                return redirect('home:home')
            
            messages.error(
                request,
                'Invalid username or password.',
                'warning'
            )
        return render(request, self.template_name, {'form': form})
    
    
    
    class UserLogoutView(View):      
       def get(self, request):
           logout(request)
           messages.success(
               request,
               'Logged out successfully',
               'success'
           )
           return redirect('home:home')
       