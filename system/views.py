from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .forms import RegistrationForm
from django.db.models import Q
from django.urls import reverse
from django.contrib.auth import authenticate, login as authLogin, logout
from datetime import datetime, timedelta
from .models import Profile, Vehicle, Booking, Maintenance

@login_required
def homepage(request):
    booking = Booking.objects.first()
    authorize = None
    if request.user.profile.UserLevel == 'Administrator':
        authorize = Vehicle.objects.all()
        
    if request.user.profile.UserLevel == 'Student' and 'Lecturer':
        authorize = booking
        
    total_count = Vehicle.objects.count()
    available_count = Vehicle.objects.filter(Status='Available').count()
    reserved_count = Vehicle.objects.filter(Status='Reserved').count()
    maintenance_count = Vehicle.objects.filter(Status='Under Maintenance').count()

    dict = {
        'booking': booking,
        'authorize':authorize,
        'total_count': total_count,
        'available_count': available_count,
        'reserved_count': reserved_count,
        'maintenance_count': maintenance_count
    }

    return render(request, 'homepage.html', dict)

def welcome(request):
    return render(request, 'welcome.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_id = form.cleaned_data.get('UserId')
            user_level = form.cleaned_data.get('UserLevel')
            phone_no = form.cleaned_data.get('PhoneNo')
            Profile.objects.create(user=user, UserLevel=user_level, PhoneNo=phone_no, UserId=user_id)
            authLogin(request, user)
            return redirect('homepage')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def logingIn(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                authLogin(request, user)
                return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logingOut(request):
    logout(request)
    return redirect('welcome')

def book(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user_level = request.user.profile.UserLevel

            # Filter vehicles based on user level
            if user_level == 'Student':
                available_vehicles = Vehicle.objects.filter(Status='Available', VehicleType__in=['Car', 'Motorcycle'])
            else:
                available_vehicles = Vehicle.objects.filter(Status='Available')

            plate_no = request.POST.get('vehicle')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')

            # Perform additional validation on start and end dates (e.g., date range, availability)

            try:
                # Check if selected vehicle is available
                selected_vehicle = Vehicle.objects.get(PlateNo=plate_no)
                if selected_vehicle.Status != 'Available':
                    messages.error(request, 'Selected vehicle is not available for booking.')
                    return redirect('book_vehicle')

                # Create a new booking entry
                booking = Booking(UserId=request.user.profile, PlateNo=selected_vehicle, StartDate=start_date, EndDate=end_date)
                booking.save()

                # Update vehicle status to Reserved
                selected_vehicle.Status = 'Reserved'
                selected_vehicle.save()

                messages.success(request, 'Vehicle booked successfully.')
                return redirect('homepage')
            except Vehicle.DoesNotExist:
                messages.error(request, 'Invalid vehicle selected.')
                return redirect('booking_details')
        else:
            messages.error(request, 'User not authenticated.')
    else:
        # Retrieve available vehicles based on user level
        if request.user.is_authenticated:
            user_level = request.user.profile.UserLevel
            if user_level == 'Student':
                available_vehicles = Vehicle.objects.filter(Status='Available', VehicleType__in=['Car', 'Motorcycle'])
            else:
                available_vehicles = Vehicle.objects.filter(Status='Available')
        else:
            available_vehicles = None

    return render(request, 'booking.html', {'vehicles': available_vehicles})

def booking_details(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id)
        return render(request, 'booking_details.html', {'booking': booking})
    except ObjectDoesNotExist:
        return render(request, 'no_booking.html')

def update_booking(request, booking_id):
    booking = Booking.objects.get(id = booking_id)
    
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        # Update booking information based on form data
        booking.StartDate = start_date
        booking.EndDate = end_date
        booking.save()
        
        # Redirect to booking details page after update
        return HttpResponse("Booking updated successfully.")
    
    return render(request, 'booking_details.html', {'booking': booking})

def delete_booking(request, booking_id):
    booking = Booking.objects.get(id = booking_id)
    
    vehicle = booking.PlateNo
    booking.delete()

    vehicle.Status = 'Available'
    vehicle.save()
    
    return HttpResponse("Booking deleted successfully.")

def add_vehicle(request):
    if request.method == 'POST':
        plate_no = request.POST.get('plate_no')
        vehicle_type = request.POST.get('vehicle_type')
        status = request.POST.get('status')
        
        if plate_no and vehicle_type:
            vehicle = Vehicle(PlateNo=plate_no, VehicleType=vehicle_type, Status=status)
            vehicle.save()
            messages.success(request, 'New Vehicle Added') 
        else:
            messages.error(request, 'Fill out all required fields')

    return render(request, 'vehicle.html')

def vehicle_status(request):
    plate_number = request.GET.get('plate_number')
    vehicles_data = Vehicle.objects.all()

    if plate_number:
        searched_vehicle = Vehicle.objects.filter(PlateNo=plate_number).first()
    else:
        searched_vehicle = None

    return render(request, 'vehicle_status.html', {
        'vehicles_data': vehicles_data,
        'searched_vehicle': searched_vehicle,
        'searched_plate_number': plate_number,
    })
            
def updateVehicle(request, PlateNo):
    updateVehi = Vehicle.objects.get(PlateNo = PlateNo)
    return render(request, "vehicle_update.html", {'updateVehi': updateVehi})
    
def update_vehicle_data(request, PlateNo):
    data = Vehicle.objects.get(PlateNo = PlateNo)
    plate_no = request.POST.get('plate_no')
    vehicle_type = request.POST.get('vehicle_type')
    status = request.POST.get('status')
    data.PlateNo = plate_no
    data.VehicleType = vehicle_type
    data.Status = status
    data.save()

    return HttpResponseRedirect(reverse("vehicle_status"))

def willDelete(request):
    will_be_delete = Vehicle.objects.all()
    return render(request, 'vehicle_delete.html', {'will_be_delete': will_be_delete})
            
def deleteVehicle(request, PlateNo):
    deleteVehi = Vehicle.objects.get(PlateNo = PlateNo)
    deleteVehi.delete()
    
    return HttpResponseRedirect(reverse("vehicle_status"))

def maintenance(request):
    vehicles = Vehicle.objects.all()
    
    if request.method == 'POST':
        plate_no = request.POST.get('plate_no')
        description = request.POST.get('description')
        last_service = request.POST.get('last_service')
        next_service = request.POST.get('next_service')

        vehicle = Vehicle.objects.get(PlateNo=plate_no)
        maintenance = Maintenance.objects.create(PlateNo=vehicle, Description=description, LastMaintenance=last_service, NextMaintenance=next_service)

        if datetime.strptime(next_service, '%Y-%m-%d').date() <= datetime.now().date():
            vehicle.Status = 'Under Maintenance'
            vehicle.save()

        return redirect('maintenance_status')  # Redirect to maintenance status page

    return render(request, 'maintenance.html', {'vehicles': vehicles})

def maintenance_status(request):
    maintenance_data = Maintenance.objects.all()
    return render(request, 'maintenance_status.html', {'maintenance_data': maintenance_data})

def updateMaintenance(request, maintenance_id):
    updateMain = Maintenance.objects.get(id=maintenance_id)
    return render(request, "maintenance_update.html", {'updateMain': updateMain})

def update_maintenance_data(request, maintenance_id):
    data = Maintenance.objects.get(id=maintenance_id)
    description = request.POST.get('description')
    last_service = request.POST.get('last_service')
    next_service = request.POST.get('next_service')
    data.Description = description
    data.LastMaintenance = last_service
    data.NextMaintenance = next_service
    data.save()

    return HttpResponseRedirect(reverse("maintenance_status"))

def viewDelete(request, maintenance_id):
    to_be_delete = Maintenance.objects.get(id=maintenance_id)
    return render(request, "maintenance_delete.html", {'to_be_delete': to_be_delete})
    
def deleteMaintenance(request, maintenance_id):
    deleteMaintenance = Maintenance.objects.get(id=maintenance_id)
    deleteMaintenance.delete()
    
    return HttpResponseRedirect(reverse("maintenance_status"))

def reset_maintenance(request, maintenance_id):
    maintenance = Maintenance.objects.get(id=maintenance_id)
    maintenance.LastMaintenance = datetime.now().date()
    maintenance.NextMaintenance = datetime.now().date() + timedelta(days=30)
    maintenance.save()
    vehicle = maintenance.vehicle
    vehicle.Status = 'Available'
    vehicle.save()
    return redirect('maintenance_status')

        
        
        
        