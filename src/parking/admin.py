from django.contrib import admin
from .models import Person,Vehicle,ParkingLot, Location
# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display=['pk', 'first_name','last_name','email','phone']
    search_fields=['first_name','last_name','email','phone']

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display=['pk', 'driver','car_type','car_plate']
    search_fields=['driver','car_type','car_plate']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display=['pk', 'name']
    search_fields=['name',]

@admin.register(ParkingLot)
class ParkingLotAdmin(admin.ModelAdmin):
    list_display=['pk', 'vehicle','available','start_time','end_time','paid_amount']
    search_fields=['vehicle','available','start_time','end_time','paid_amount']
    list_filter = ['location', 'available']

