from django.shortcuts import render, redirect
from django.contrib.auth import login, authentication
from .forms import LoginForm
from django.http import HttpRequest, HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authentication(request, username = cd['username'], password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Success")
                else:
                    return HttpResponse("Not Active")
            return HttpResponse("Invalid")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form':form})