from django.urls import path
from .views import Home, About, Main, CarsView

app_name = "Home"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("about/", About.as_view(), name="about"),
    path("main/<int:id>/<str:name>/", Main.as_view(), name="main"),
    path("cars/", CarsView.as_view(), name="cars"),
]
