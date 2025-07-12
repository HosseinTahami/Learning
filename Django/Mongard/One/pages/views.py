from django.shortcuts import render

def home(request):
    person = {"Name": "admin", "Age": 23}
    return render(request, "home.html", person)

