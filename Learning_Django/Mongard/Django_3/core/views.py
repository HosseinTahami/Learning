# Django Imports

from django.shortcuts import render
from django.views import View

# Project Imports

from .models import Product, Category


class HomePageView(View):

    def get(self, request):
        products = Product.objects.filter(available=True)
        return render(request, 'core/home.html', {'products': products})


class ProductDetailView(View):

    def get(self, request, product_slug):
        product = Product.objects.get(slug=product_slug)
        return render(request, 'core/product_detail.html', {'product': product})
