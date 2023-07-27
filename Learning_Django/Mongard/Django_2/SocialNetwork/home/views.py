from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, 'home/index.html')    

    def post(self, request):
        return render(request, 'home/index.html')