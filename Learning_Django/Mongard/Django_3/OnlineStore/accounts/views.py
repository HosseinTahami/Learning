from django.shortcuts import render
from django.views import View

class UserRegisterView(View):
    def get(self, request):
        #return render(request, 'home/index.html')
        pass
    def post(self, request):
        pass