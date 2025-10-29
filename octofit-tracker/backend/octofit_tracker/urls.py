from django.contrib import admin
from django.urls import path, include
from .views import api_root, router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", api_root, name="api-root"),
    path("api/", include(router.urls)),
]
