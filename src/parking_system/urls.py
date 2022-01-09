
from django import views
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from parking.views import (home,payment_cancelled,payment_done,
process_payment,LogoutView,LoginView,VehicleView, ParkingLotView)
from django.conf import settings
from django.conf.urls.static import static
from parking.views import RegisterUserView,LogoutView,LoginView,redirect_view

urlpatterns = [
    path('parking/login/', LoginView.as_view(), name='login'),
    path('parking/register/', RegisterUserView.as_view(), name='user_register'),
    path('parking/logout/', LogoutView.as_view(), name='logout'),
    path('parking/vehicles/', VehicleView.as_view(), name='vehicles'),
    path('parking/parking-lots/', ParkingLotView.as_view(), name='parking_lots'),
    path('admin/', admin.site.urls),
    path('accounts/profile/', redirect_view),
    # path('parking/',RegisterView.as_view(),name='register'),
    path('',home,name='home' ),
    path('paypal/',include('paypal.standard.ipn.urls')),
    path('process-payment/',process_payment,name='process_payment'),
    path('payment-done/',payment_done,name='payment_done'),
    path('payment-cancelled/',payment_cancelled,name='payment_cancelled')
   
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
