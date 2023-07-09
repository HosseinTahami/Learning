from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    person = { 'name' : 'Hossein'}
    return render(request, 'home.html', context=person)

def say_hello(request):
    return HttpResponse(" Hello MFs!")

def say_bye(request):
    return render(request, 'bye.html')