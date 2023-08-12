from typing import Any, Optional
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import TemplateView, RedirectView, ListView
from .models import Car


class Home(View):
    http_method_names = [
        "get",
        "post",
        "option",
    ]

    def setup(self, *args, **kwargs):
        self.users = User.objects.all()
        super().setup(self, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET":
            return self.get(request)
        elif request.method == "POST":
            return self.post(request)
        elif request.method == "OPTIONS":
            return self.options(request)
        else:
            raise ("Method Not Allowed")

    def get(self, request):
        # users = User.object.all()
        return render(request, "Home/home.html", {"users": self.users})

    def post(self, request):
        # users = User.object.all()
        return render(request, "Home/home.html", {"users": self.users})

    def options(self, request, *args, **kwargs):
        response = super().options(request, *args, **kwargs)
        response.headers["host"] = "localhost"
        response.headers["user"] = request.user
        return response

    def http_method_not_allowed(self, request, *args, **kwargs):
        super().http_method_not_allowed(request, *args, **kwargs)
        return render(request, "method_not_allowed.html")


class About(TemplateView):
    template_name = "Home/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cars"] = Car.objects.all()
        return context


class Main(RedirectView):
    url = "https://www.mongard.ir"
    # pattern_name = "Home:about"
    # url = "/home/%(id)i/%(name)s"
    # query_string = True

    # def get_redirect_url(self, *args: Any, **kwargs: Any):
    #     print(kwargs["name"], kwargs["id"])  # .../main/hossein/12
    #     return super().get_redirect_url(*args, **kwargs)


class CarsView(ListView):
    template_name = "Home/cars.html"
    model = Car  # --> object_list
