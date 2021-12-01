from django.shortcuts import render
from django.views import View
from .form import PersonForm,VehicleForm,ParkingLotForm

def home(request):
    return render(request,'parking/home.html')
class RegisterView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'parking/register.html',{'person_form':PersonForm,'vehicle_form':VehicleForm,'parking_form':ParkingLotForm})

