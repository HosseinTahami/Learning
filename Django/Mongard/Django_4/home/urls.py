from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('home/1/', views.home, name='function_home'),  # end-point
    path('home/2/<str:first_name>/', views.AnotherHomeView.as_view(),  # GET: home/Hossein/?last_name=Tahami
         name='first_class_home'),  # end-point
    path('home/3/', views.HomeView.as_view(), name='second_class_home'),
    path('person/', views.PersonView.as_view(), name='person'),
]
