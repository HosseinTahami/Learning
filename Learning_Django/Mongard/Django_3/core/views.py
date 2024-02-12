# Django Imports

from django.shortcuts import render
from django.views import View

# Project Imports


class HomePageView(View):

    def get(self, request):
        return render(request, 'core/home.html')
