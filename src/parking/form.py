from django import forms
from django.forms import ModelForm, widgets
from .models import ParkingLot,Person,Vehicle


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email','phone', 'password1', 'password2')

class SelectParkingLot(forms.Form):
    vehicle = forms.CharField()
    available_parking_lots = forms.ModelChoiceField(
        queryset=ParkingLot.objects.filter(available=True)
    )
    duration = forms.DurationField(help_text="Duration in hours")

    def __init__(self, *args, **kwargs):
        current_user_id = kwargs.pop('user_id')
        super().__init__(*args, **kwargs)
        allocated_vehicles = list(ParkingLot.objects.filter(
            vehicle_id__isnull=False).values_list('vehicle__id', flat=True))
        self.fields['vehicle'] = forms.ModelChoiceField(
            queryset=Vehicle.objects.filter(driver_id=int(current_user_id)).exclude(
                id__in=allocated_vehicles
            ))


class LoginForm(AuthenticationForm):
    pass
class PersonForm(ModelForm):
    class Meta:
        model=Person
        fields='__all__'
class VehicleForm(ModelForm):
    class Meta:
        model=Vehicle
        fields='__all__'
        widgets={'driver': widgets.HiddenInput()}
class ParkingLotForm(ModelForm):
    class Meta:
        model=ParkingLot
        fields='__all__'
        widgets={'vehicle':widgets.HiddenInput()}