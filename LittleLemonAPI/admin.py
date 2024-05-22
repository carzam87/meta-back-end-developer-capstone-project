from django.contrib import admin

from .models import MenuItem,Booking

# Register your models here.
admin.site.register(MenuItem)


class BookingAdmin(admin.ModelAdmin):
    list_display = ['id','name','no_of_guests','booking_date']
    list_filter = ['booking_date']
    search_fields = ['name']
    ordering = ['booking_date']
    list_per_page = 10

admin.site.register(Booking, BookingAdmin)

