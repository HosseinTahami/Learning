from django.urls import path
from .views import Home, About, Main, CarsView, CarDetailView

app_name = "Home"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("about/", About.as_view(), name="about"),
    path("main/<int:id>/<str:name>/", Main.as_view(), name="main"),
    path("cars/", CarsView.as_view(), name="cars"),
    path("cars_detail/<int:car_id>", CarDetailView.as_view(), name="cars_detail"),
    # path("cars_detail/<slug:my_slug>", CarDetailView.as_view(), name="cars_detail"),
    # path("cars_detail/<str:name>/<int:build_year>/<str:owner>/", CarDetailView.as_view(), name="cars_detail"),
]
