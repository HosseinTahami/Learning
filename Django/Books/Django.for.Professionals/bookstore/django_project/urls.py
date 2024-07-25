from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Django Admin
    path("admin/", admin.site.urls),
    # User Management
    path("accounts/", include("allauth.urls")),
    #   path("accounts/", include("django.contrib.auth.urls"))
    # Local Apps
    path("", include("pages.urls")),
    path("books/", include("books.urls")),
    #   path("accounts/", include("accounts.urls"))
] + static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:

    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
