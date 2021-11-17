from django.contrib import admin
from .models import Person,Vehicle,ParkingLot
# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display=['first_name','second_name','email','phone']
    search_fields=['first_name','second_name','email','phone']

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display=['driver','car_type','car_plate']
    search_fields=['driver','car_type','car_plate']

@admin.register(ParkingLot)
class ParkingLotAdmin(admin.ModelAdmin):
    list_display=['vehicle','available','start_time','end_time','paid_amount']
    search_fields=['vehicle','available','start_time','end_time','paid_amount']

