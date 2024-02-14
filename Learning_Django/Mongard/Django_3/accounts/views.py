# Django Imports

from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

# Project Imports

from .forms import UserRegisterForm, VerifyCodeForm
from .models import User, OTP
from utils import send_otp


class UserRegisterView(View):

    template_name = 'accounts/register.html'
    form_class = UserRegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            code = OTP.code_creator(self)
            cd = form.cleaned_data
            send_otp(cd['phone_number'], code)
            OTP.objects.create(phone_number=cd['phone_number'], code=code)
            request.session['user_registration_data'] = {
                'phone_number': cd['phone_number'],
                'email': cd['email'],
                'first_name': cd['first_name'],
                'last_name': cd['last_name'],
                'password': cd['password']
            }
            messages.success(request, 'We sent you a code.', 'success')
            return redirect('accounts:verify_code')
        return redirect('core:home')


class UserRegisterVerifyCodeView(View):
    form_class = VerifyCodeForm

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/verify.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user_session = request.session['user_registration_data']
            OTP_instance = OTP.objects.get(
                phone_number=user_session['phone_number'])
            if cd['code'] == OTP_instance.code:
                User.objects.create_user(user_session['phone_number'], user_session['email'],
                                         user_session['first_name'], user_session['last_name'], user_session['password'])
                OTP_instance.delete()
                messages.success(request, 'You are registered successfully')
                return redirect('core:home')

            messages.error(request, 'Wrong Code', 'danger')
            return redirect('accounts:verify_code')
