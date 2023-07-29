from django.shortcuts import render
from django.views import View
from .forms import UserRegistrationForm


class UserRegisterView(View):
    
    form_class = UserRegistrationForm
    template = 'accounts/register.html'
    
    def get(self, request):
        form = self.form_class
        return render(request, self.template, {'form': form})
    
    def post(self, request):
        pass