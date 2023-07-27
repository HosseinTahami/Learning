from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm

class UserRegister(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request,
                      'accounts/register.html',
                      {'form': form}
                    )
    def post(self, request):
        pass

