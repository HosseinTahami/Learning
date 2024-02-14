# Django Imports

from django.urls import path

# Project Imports

from . import views

app_name = 'core'

urlpatterns = [

    path('', views.HomePageView.as_view(), name='home'),
    path('<slug:product_slug>/',
         views.ProductDetailView.as_view(), name='product_detail'),
]
