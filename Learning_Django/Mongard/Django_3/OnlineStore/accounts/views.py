from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm
from django.contrib import messages
from utils import send_top_code
import random
from .models import OtpCode

class UserRegisterView(View):
    form_class = UserRegistrationForm
    template = "accounts/register.html"

    def get(self, request):
        form = self.form_class
        return render(request, self.template, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            random_code = random.randint(1000, 9999)
            send_top_code(cd['phone_number'], random_code)
            OtpCode.objects.create(
                phone_number=cd['phone_number'],
                code=random_code
                )
            request.session['user_registration_info'] = {
                'phone_number': cd['phone_number'],
                'email': cd['email'],
                'full_name': cd['full_name'],
                'password': cd['password'],
            }
            messages.success(request, 'You have successfully registered.', 'success')
            return redirect('accounts:verify_code')
        return redirect('home:home')
    
class VerifyCodeView(View):
    
    def get(self, request):
        pass
    
    def post(self, request):
        pass
    