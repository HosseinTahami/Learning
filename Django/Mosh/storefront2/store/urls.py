from django.urls import path
from . import views
urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:product_id>/', views.product_detail),
    path('collections/<int:pk>/', views.collection_detail,
         name='collection_detail'),
    path('collections/', views.collection_list),

]
