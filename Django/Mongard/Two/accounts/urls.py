from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("register/", views.UserRegisterView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path("profile/<int:pk>/", views.UserProfileView.as_view(), name="profile"),
    path("profile/edit/", views.UpdateProfileView.as_view(), name="profile_update"),
    # Reset Password
    path("password/reset/", views.UserPasswordResetView.as_view(), name="password_reset"),
    path("password/reset/done/", views.UserPasswordResetDoneView.as_view(), name="password_reset_done"),
    path("password/reset/confirm/<uidb64>/<token>/", views.UserPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("password/reset/complete/", views.UserPasswordResetCompleteView.as_view(), name="password_reset_complete"),
    # Relations
    path("follow/<int:pk>/", views.FollowView.as_view(), name="follow"),
    path("unfollow/<int:pk>/", views.UnfollowView.as_view(), name="unfollow"),
    
]
