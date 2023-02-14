from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    # Login Authentications 
    path('partner-login/',views.partnerLogin, name='partnerLogin'),
    path('partner-logout/',views.partnerLogout, name='partnerLogout'),
    path('new-registration/',views.newRegistrations, name='newRegistrations'),
    
    
    path('',views.home, name='home'),
    path('vendor-details/',views.vendorDetails, name='vendorDetails'),
    
    # Booking URLS 
    path('bookings/',views.bookings, name='bookings'),
    path('booking-details/',views.bookingDetails, name='bookingDetails'),
    
    
    # Hotels Management 
    path('hotels/',views.hotels, name='hotels'),
    path('add-new-hotel/',views.AddNewHotel, name='AddNewHotel'),
    path('delete-hotel/<int:id>/',views.deleteHotel, name='deleteHotel'),
    
    path('add-new-room/<str:slug>/',views.AddNewRoom, name='AddNewRoom'),
    
    path('property-details/<str:slug>/',views.propertyDetails, name='propertyDetails'),
    
    
]   