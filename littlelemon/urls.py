"""littlelemon URL Configuration"""

from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

# from restaurant.views import BookingViewSets, UserViewSet



router = DefaultRouter()
# router.register(r"users", UserViewSet, basename="user")
# router.register(r"tables", BookingViewSets)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("LittleLemonAPI.urls")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
    # path("restaurant/booking/", include(router.urls)),
]
