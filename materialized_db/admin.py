from django.contrib import admin

from .models import Bookings, Facility, Members

admin.site.register((Facility, Members, Bookings))
