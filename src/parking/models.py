from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.base_user import BaseUserManager

class PersonManager(BaseUserManager):
    def _create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, password, **kwargs)

    
    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        return self._create_user(email, password, **kwargs)

class Person(AbstractUser):
    email=models.EmailField(max_length=250, unique=True)
    phone=models.CharField(max_length=50)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    username = None

    objects = PersonManager()


class Vehicle(models.Model):
    CAR_TYPES=[
        ('SALOON','SALOON'),
        ('HEAVY DUTY','HEAVY DUTY'),
        ('SUV','SUV'),
    ]
    driver=models.ForeignKey(Person, on_delete=models.CASCADE)
    car_type=models.CharField(max_length=100,choices=CAR_TYPES)
    car_plate=models.CharField(max_length=15, unique=True)

    def __str__(self) -> str:
        return f"{self.car_plate} - {self.car_type}"



class Location(models.Model):
    name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name

class ParkingLot(models.Model):
    vehicle=models.OneToOneField(Vehicle,null=True,blank=True,on_delete=models.SET_NULL, unique=True)
    available=models.BooleanField(default=False)
    start_time=models.DateTimeField(null=True,blank=True)
    end_time=models.DateTimeField(null=True,blank=True)
    paid_amount=models.IntegerField(null=True,blank=True)
    location = models.ForeignKey(Location, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f"Parking {self.pk}: {self.location.name}"

