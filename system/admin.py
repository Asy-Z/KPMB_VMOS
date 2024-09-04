from django.contrib import admin
from . models import Profile, Vehicle, Booking, Maintenance

# Register your models here.
admin.site.register(Profile)
admin.site.register(Vehicle)
admin.site.register(Booking)
admin.site.register(Maintenance)