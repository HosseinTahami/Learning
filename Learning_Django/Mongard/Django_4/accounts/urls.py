# Django imports
from django.urls import path
#from rest_framework.authtoken import views as auth_token
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Inside Project Imports
from . import views

app_name = "accounts"

urlpatterns = [
    path("register/", views.UserRegister.as_view(), name="register"),
    #path("auth_token_creation/", auth_token.obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = routers.SimpleRouter()
router.register('user', views.UserViewSet)
urlpatterns += router.urls