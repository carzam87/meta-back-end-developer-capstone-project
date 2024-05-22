from django.contrib.auth.models import User

from rest_framework import serializers
from .models import MenuItem, Booking



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id','name','no_of_guests','booking_date']
        
    def validate(self, data):
        # Create an instance of the Booking model
        booking = Booking(**data)
        # Call the clean method
        booking.clean()
        return data

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], password=validated_data['password'])
        return user