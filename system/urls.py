from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("homepage/", views.homepage, name="homepage"),
    path("booking/", views.book, name="booking"),
    path('booking/<int:booking_id>/', views.booking_details, name='reservation'),
    path('booking/<int:booking_id>/update/', views.update_booking, name='update_booking'),
    path('booking/<int:booking_id>/delete/', views.delete_booking, name='delete_booking'),
    path("register/", views.register, name="register"),
    path("login/", views.logingIn, name="login"),
    path("logout/", views.logingOut, name="logout"),
    path("vehicle/", views.add_vehicle, name="vehicle"),
    path('vehicle/vehicle_status/', views.vehicle_status, name='vehicle_status'),
    path('vehicle/vehicle_update/<str:PlateNo>', views.updateVehicle, name='updateVehicle'),
    path('vehicle/vehicle_update/update_vehicle_data/<str:PlateNo>', views.update_vehicle_data, name='update_vehicle_data'),
    path('vehicle/vehicle_delete/<str:PlateNo>', views.willDelete, name='deleteVehicle'),
    path('vehicle/vehicle_delete/delete_vehicle_data/<str:PlateNo>', views.deleteVehicle, name='deleteVehicle'),
    path('maintenance/', views.maintenance, name='maintenance'),
    path('maintenance/maintenance_status/', views.maintenance_status, name='maintenance_status'),
    path('maintenance/maintenance_update/<int:maintenance_id>', views.updateMaintenance, name='updateMaintenance'),
    path('maintenance/maintenance_update/update_maintenance_data/<int:maintenance_id>', views.update_maintenance_data, name='update_maintenance_data'),
    path('maintenance/maimtenance_delete/<int:maintenance_id>', views.viewDelete, name='deleteMaintenance'),
    path('maintenance/maimtenance_delete/delete_maintenance_data/<int:maintenance_id>', views.deleteMaintenance, name='deleteMaintenance'),
    path('maintenance/reset/<int:maintenance_id>/', views.reset_maintenance, name='reset_maintenance'),
]

