from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView

from rest_framework.permissions import IsAuthenticated

from .serializers import MenuItemSerializer, RegistrationSerializer, BookingSerializer

from .models import MenuItem, Booking
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

class MenuItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class RegistrationView(APIView):
    def post(self, request):
        # Create a new user
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)