# Django imports
from django.urls import path

# Project imports
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('post/<int:post_id>/<slug:post_slug>/',
         views.PostDetailView.as_view(), name='post_detail'),
]
