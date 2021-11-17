from django.db import models

class Person(models.Model):
    first_name=models.CharField(max_length=30)
    second_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=250)
    phone=models.CharField(max_length=50)
class Vehicle(models.Model):
    CAR_TYPES=[
        ('S','SALOON'),
        ('T','HEAVY DUTY'),
        ('X','SUV'),
    ]
    driver=models.ForeignKey(Person, on_delete=models.CASCADE)
    car_type=models.CharField(max_length=1,choices=CAR_TYPES)
    car_plate=models.CharField(max_length=15)
class ParkingLot(models.Model):
    vehicle=models.OneToOneField(Vehicle,null=True,blank=True,on_delete=models.SET_NULL)
    available=models.BooleanField(default=False)
    start_time=models.DateField()
    end_time=models.DateField()
    paid_amount=models.IntegerField()
