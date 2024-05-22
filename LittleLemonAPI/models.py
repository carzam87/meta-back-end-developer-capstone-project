from django.db import models
from datetime import timedelta
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return f"{self.title} : {str(self.price)}"


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()

        end_time = self.booking_date + timedelta(minutes=30)

        overlapping_bookings = Booking.objects.filter(
            booking_date__lt=end_time,
            booking_date__gt=self.booking_date - timedelta(minutes=30),
        ).exclude(id=self.id)

        if overlapping_bookings.exists():
            raise ValidationError(_("This booking overlaps with another booking."))
