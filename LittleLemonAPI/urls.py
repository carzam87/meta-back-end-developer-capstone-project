from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, BookingViewSet, RegistrationView

router = DefaultRouter()
router.register(r'menu-items', MenuItemViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
        path('', include(router.urls)),
        path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
        path('register/', RegistrationView.as_view()),
]