from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegistrationForm
def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            pass
    else:
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form':form})
        
