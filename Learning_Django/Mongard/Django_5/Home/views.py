from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User


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
