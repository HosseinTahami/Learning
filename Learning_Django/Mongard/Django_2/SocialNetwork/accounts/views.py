from django.shortcuts import render, redirect
from django.views import View


class UserRegister(View):
    def get(self, request):
        return render(request, 'accounts/register.html')
    def get(self, request):
        pass

