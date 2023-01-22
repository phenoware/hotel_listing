from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    # Login Authentications 
    path('',views.home, name='home'),
    path('admin-logout/',views.adminLogout, name='adminLogout'),

]