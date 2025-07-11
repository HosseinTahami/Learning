from django.shortcuts import render
from django.views import View

class HomePageView(View):

    def get(self, request, *args, **kwargs):
        return render(request=request, template_name="pages/home.html")