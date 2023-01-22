from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    # Login Authentications 
    path('',views.home, name='home'),
    path('customer-details/',views.customerDetails, name='customerDetails'),
    
    path('bookings/',views.bookings, name='bookings'),
    path('booking-details/',views.bookingDetails, name='bookingDetails'),
    
    
]