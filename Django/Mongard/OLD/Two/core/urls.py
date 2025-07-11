from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls", namespace="pages")),
    path("posts/", include("posts.urls", namespace="posts")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
]
