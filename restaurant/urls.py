from django.urls import include, path
from .views import MenuItemsView, BookingView, SingleMenuItemView


urlpatterns = [
    path("menu/", MenuItemsView.as_view()),
    path("menu/<int:pk>", SingleMenuItemView.as_view()),
    path("bookings/", BookingView.as_view(), name="booking"),
]
