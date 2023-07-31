from django.shortcuts import render
from django.views import View
from .forms import UserRegistrationForm
from utils import send_top_code
import random

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
