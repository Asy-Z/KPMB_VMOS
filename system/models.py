from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    UserId = models.CharField(max_length = 12, primary_key = True, unique =True)
    
    USERTYPE = [
    ('Administrator', 'Administrator'),
    ('Student', 'Student'),
    ('Lecturer', 'Lecturer')
    ]
    
    UserLevel = models.TextField(max_length = 30, choices = USERTYPE)
    PhoneNo = models.CharField(max_length = 12)
    
class Vehicle(models.Model):
    PlateNo = models.CharField(max_length = 10, primary_key = True)
    
    VEHICLETYPE = [
        ('Van', 'Van'),
        ('Car', 'Car'),
        ('Motorcycle', 'Motorcycle'),
        ('Bus', 'Bus')
    ]
    
    VehicleType = models.TextField(max_length = 30, choices = VEHICLETYPE, default = 'Van')
    
    STATUSTYPE = [
    ('Available', 'Available'),
    ('Reserved', 'Reserved'),
    ('Under Maintenance', 'Under Maintenance')
    ]

    Status = models.TextField(max_length = 30, choices = STATUSTYPE, default = 'Available')
    
class Booking(models.Model):
    UserId = models.ForeignKey(Profile, on_delete = models.CASCADE)
    PlateNo = models.ForeignKey(Vehicle, on_delete = models.CASCADE)
    StartDate = models.DateField(null = True, blank = True)
    EndDate = models.DateField(null = True, blank = True)
    
class Maintenance(models.Model):
    PlateNo = models.ForeignKey(Vehicle, on_delete = models.CASCADE)
    Description = models.TextField(max_length = 50)
    LastMaintenance = models.DateField(null = True, blank = True)
    NextMaintenance = models.DateField(null = True, blank = True)