"""littlelemon URL Configuration"""

from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("LittleLemonAPI.urls")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path("restaurant/", include("restaurant.urls")),
]
