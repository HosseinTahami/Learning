from django.shortcuts import render
from django.views import View
from . import forms


class RegistrationView(View):

    def get(self, request):
        form = forms.RegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        ...
