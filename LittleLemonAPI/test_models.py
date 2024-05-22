from django.test import TestCase
from django.contrib.auth.models import User
from LittleLemonAPI.models import Booking, MenuItem


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(
            title="Ice Cream", price=80, inventory=100
        )
        itemstr = item.__str__()
        self.assertEqual(itemstr, "Ice Cream : 80")


class BookingTest(TestCase):
    def test_get_booking(self):
        booking = Booking.objects.create(
            name="John Doe", no_of_guests=2, booking_date="2021-10-10"
        )
        bookingstr = booking.__str__()
        self.assertEqual(bookingstr, "John Doe")

class RegistrationTest(TestCase):
    def test_get_registration(self):
        new_user = User.objects.create(
            username="johndoe", email="john@example.com", password="password"
        )
        # Check if the user was created
        self.assertIsNotNone(new_user)
        # Check if the user's name is correct
        self.assertEqual(new_user.username, "johndoe")
        # Check if the user's email is correct
        self.assertEqual(new_user.email,   "john@example.com")
        # Check if the user's password is correct
        self.assertEqual(new_user.password, "password")
        
