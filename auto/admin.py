from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "service", "date", "time")
    list_filter = ("service", "date")
    search_fields = ("name", "phone", "email", "car_model")
    ordering = ("-date", "-time")

