from django.forms import ModelForm, fields, models
from .models import ParkingLot,Person,Vehicle

class PersonForm(ModelForm):
    class Meta:
        model=Person
        fields='__all__'
class VehicleForm(ModelForm):
    class Meta:
        model=Vehicle
        fields='__all__'
class ParkingLotForm(ModelForm):
    class Meta:
        model=ParkingLot
        fields='__all__'