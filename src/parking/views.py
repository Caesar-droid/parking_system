from django.conf import settings
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
from django.shortcuts import get_object_or_404, redirect, render
# from django.template import RequestContext
from django.views import View
from .models import ParkingLot, Vehicle
from .form import PersonForm,VehicleForm,ParkingLotForm, SelectParkingLot
from django.contrib.auth import views as auth_views
from django.views import generic
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils import timezone


from .form import LoginForm, RegisterForm


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'parking/login.html'


class RegisterUserView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'parking/user_register.html'
    success_url = reverse_lazy('login')


class LogoutView(auth_views.LogoutView):
    template_name = 'parking/logout.html'

def redirect_view(request):
    response = redirect('/')
    return response
def home(request):
    return render(request,'parking/home.html')

class VehicleView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'parking/vehicles.html',{
            'vehicles':Vehicle.objects.filter(driver=request.user),
            'form': VehicleForm()
        })

    def post(self,request,*args,**kwargs):
        post_data=request.POST.copy()
        post_data['driver']=request.user.pk
        form = VehicleForm(post_data)
        if form.is_valid():
            form.save()
            return render(request,'parking/vehicles.html',{
                'vehicles':Vehicle.objects.filter(driver=request.user),
                'form': form
            })
        return redirect('vehicles')

class ParkingLotView(View):
    def get(self,request,*args,**kwargs):
        context = self._get_context(request)
        return render(request,'parking/parking_lots.html', context)

    def _get_context(self, request):
        my_vehicles = Vehicle.objects.filter(driver=request.user)
        allocated_parking_lots = ParkingLot.objects.filter(
            vehicle__in=my_vehicles, 
            available=False
        )
        available_parking_lots = ParkingLot.objects.filter(
            available=True
        )
        form = SelectParkingLot(user_id=request.user.pk)
        return {
            'form': form,
            'allocated_lots': allocated_parking_lots,
            'available_lots': available_parking_lots
        }

    def post(self,request,*args,**kwargs):
        form = SelectParkingLot(request.POST, user_id=request.user.pk)
        if form.is_valid():
            data = form.cleaned_data
            selected_lot = data['available_parking_lots']
            selected_vehicle = data['vehicle']
            duration = data['duration'] * 60 * 60
            start_time = timezone.now()
            end_time = start_time + duration
            lot = ParkingLot.objects.get(id=selected_lot.id)
            lot.vehicle = selected_vehicle
            lot.start_time=  start_time
            lot.end_time = end_time
            lot.available= False
            lot.save()
            return redirect('process_payment')

        context = self._get_context(request)
        context['form'] = form
        return render(request,'parking/parking_lots.html',context)

# class RegisterView(View):
#     def get(self,request,*args,**kwargs):
#         print(request)
#         return render(request,'parking/register.html',{'person_form':PersonForm,'vehicle_form':VehicleForm,'parking_form':ParkingLotForm })

#     def post(self,request,*args,**kwargs):
#         post_data=request.POST.copy()
#         post_data['driver']=request.user.pk
#         vform=VehicleForm(post_data)
#         if vform.is_valid():
#             vehicle=vform.save()
#             post_data=request.POST.copy()
#             post_data['vehicle']=vehicle.pk
#         lform=ParkingLotForm(post_data)
#         if lform.is_valid():
#             lform.save()
#         return redirect('/process-payment/')
#         return render(request,'parking/home.html')
def process_payment(request):
    pay=request.session.get('paid_amount')
    # amount=get_object_or_404(ParkingLot,id=pay)
    host=request.get_host()

    paypal_dict={
        'business':settings.PAYPAL_RECEIVER_EMAIL,
        'amount':500,
        'plan':'ParkingLot{}'.format(pay),
        'invoice_item': str(ParkingLot.id),
        'currency_code':'KES',
        'notify_url':'http://{}{}'.format(host,reverse('paypal-ipn')),
        'return_url':'http://{}{}'.format(host,reverse('payment_done')),
        'cancel_return':'http://{}{}'.format(host,reverse('payment_cancelled')),
    }
    form=PayPalPaymentsForm(initial=paypal_dict)
    return render(request,'parking/make_payment.html',{'form':form})

@csrf_exempt
def payment_done(request):
    return render(request,'parking/payment_done.html')
@csrf_exempt
def payment_cancelled(request):
    return render(request,'parking/payment_cancelled.html')

    