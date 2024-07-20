from django.views.generic import ListView
from . import models

class HomePageView(ListView):
    model = models.Post
    template_name = "home.html"

