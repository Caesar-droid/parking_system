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

    def post(request,*args,**kwargs):
        if request.GET == True:
            pform=PersonForm(request.POST)
            vform=VehicleForm(request.POST)
            lform=ParkingLotForm(request.POST)
            if pform.is_valid()  and vform.is_valid() and lform.is_valid() :
                pform.save()
                vform.save()
                lform.save() 
            return render(request,'parking/home.html')
# def register(request):
#      if request.GET == True:
#             pform=PersonForm(request.POST)
#             vform=VehicleForm(request.POST)
#             lform=ParkingLotForm(request.POST)
#             if pform.is_valid()  and vform.is_valid() and lform.is_valid() :
#                 pform.save()
#                 vform.save()
#                 lform.save() 
#             return render(request,'parking/home.html',context_instance=RequestContext(request))
#      elif request.method == "GET":
#         return render(request,'parking/register.html',{'person_form':PersonForm,'vehicle_form':VehicleForm,'parking_form':ParkingLotForm })
    