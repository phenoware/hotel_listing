from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from .models import *

from django.conf import settings
from django.core.mail import send_mail

def home(request):
    return render(request ,'partner/vendor.html')   

def vendorDetails(request):
    return render(request,'partner/vendor-details.html')