from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegistrationForm


class UserRegisterView(View):
    from_class = UserRegistrationForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.from_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.from_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            User.objects.create_user(
                cd['username'], cd['email'], cd['password'])
            messages.success(
                request, 'User Registered Successfully !', 'success')
            return redirect('core:home')
        return render(request, self.template_name, {'form': form})
