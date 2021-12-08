from django.shortcuts import render
# from django.template import RequestContext
from django.views import View
from .form import PersonForm,VehicleForm,ParkingLotForm

def home(request):
    return render(request,'parking/home.html')
class RegisterView(View):
    def get(self,request,*args,**kwargs):
        print(request)
        return render(request,'parking/register.html',{'person_form':PersonForm,'vehicle_form':VehicleForm,'parking_form':ParkingLotForm })

    def post(self,request,*args,**kwargs):
       
        pform=PersonForm(request.POST)
        if pform.is_valid():
            person=pform.save()
            post_data=request.POST.copy()
            post_data['driver']=person.pk
        vform=VehicleForm(post_data)
        if vform.is_valid():
            vehicle=vform.save()
            post_data=request.POST.copy()
            post_data['vehicle']=vehicle.pk
        lform=ParkingLotForm(post_data)
        if lform.is_valid():
            lform.save()
        return render(request,'parking/home.html')

    