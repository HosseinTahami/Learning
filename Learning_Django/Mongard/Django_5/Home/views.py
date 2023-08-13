from typing import Any, Optional
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import (
    TemplateView,
    RedirectView,
    ListView,
    DetailView,
    FormView,
)
from .models import Car
from .forms import CreateCarForm
from django.urls import reverse_lazy


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
    # model = Car  # --> object_list
    context_object_name = "cars"
    # queryset = Car.objects.filter(build_year__gt=1930)

    def get_queryset(self):
        result = Car.objects.filter(build_year__gt=1990)
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["specific_title"] = "New Car List:"
        return context


class CarDetailView(DetailView):
    template_name = "Home/car_detail.html"
    model = Car
    context_object_name = "car"
    pk_url_kwarg = "car_id"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Car.objects.filter(pk=self.kwargs["car_id"])
        else:
            return Car.objects.none()


# class CarDetailView(DetailView):
#     template_name = "Home/car_detail.html"
#     model = Car
#     slug_field = "name"
#     slug_url_kwarg = "my_slug"


# class CarDetailView(DetailView):
#     template_name = "Home/car_detail.html"

#     def get_object(self, queryset=None):
#         return Car.objects.get(
#             name=self.kwargs["name"],
#             owner=self.kwargs["owner"],
#             build_year=self.kwargs["build_year"],
#         )  # --> in the html file href={% url 'Home:cars_detail' car.name car.owner car.build_year %}


class CreateCarView(FormView):
    template_name = "Home/create_car.html"
    form_class = CreateCarForm
    success_url = reverse_lazy("Home:home")

    def form_valid(self, form):
        self._create_car_(form.cleaned_data)
        return super().form_valid(form)

    def _create_car_(self, data):
        Car.objects.create(
            brand=data["brand"],
            owner=data["owner"],
            build_year=data["build_year"],
        )
