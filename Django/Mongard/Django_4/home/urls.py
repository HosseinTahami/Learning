from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='function_home'),
    path('home/', views.HomeView.as_view(), name='class_home')
]
