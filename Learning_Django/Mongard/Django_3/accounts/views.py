# Django Imports

from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

# Project Imports

from .forms import UserRegisterForm
from .models import User, OTP


class UserRegisterView(View):

    template_name = 'accounts/register.html'
    form_class = UserRegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        code = OTP.code_creator()
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code:
                User.objects.create_user(
                    first_name=cd['first_name'],
                    last_name=cd['last_name'],
                    phone_number=cd['phone_number']
                )
                messages.success(request, 'Account Created', 'success')
                return redirect('core:home')
            messages.error(request, 'Wrong OTP', 'danger')
        return render(request, self.template_name)
