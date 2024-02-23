# Django Imports

from django.shortcuts import render, get_object_or_404
from django.views import View

# Project Imports

from .models import Product
from .tasks import all_bucket_objects_task


class HomePageView(View):

    def get(self, request):
        products = Product.objects.filter(available=True)
        return render(request, 'core/home.html', {'products': products})


class ProductDetailView(View):

    template_name = 'core/product_detail.html'

    def get(self, request, product_slug):
        product = get_object_or_404(Product, slug=product_slug)
        return render(request, self.template_name, {'product': product})


class BucketHome(View):
    template_name = 'core/bucket.html'

    def get(self, request):
        objects = all_bucket_objects_task()
        print('*'*90)
        print(objects)
        return render(request, self.template_name, {'objects': objects})
