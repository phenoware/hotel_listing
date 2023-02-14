from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('hotel-details/',views.hotelDetails, name='hotelDetails'),
    path('book-now/',views.bookNow, name='bookNow'),

    path('user-login/',views.userLogin, name='userLogin'),
    path('user-register/',views.userRegister, name='userRegister'),
    
       
]