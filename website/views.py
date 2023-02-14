from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    try:
        return render(request, 'website/index.html')
    except Exception as e:
        return  HttpResponse(e)


def hotelDetails(request):
    try:
        return render(request, 'website/hotel-details.html')
    except Exception as e:
        return  HttpResponse(e)


def bookNow(request):
    try:
        return render(request, 'website/book-now.html')
    except Exception as e:
        return  HttpResponse(e)


def userLogin(request):
    try:
        return render(request, 'website/login.html')
    except Exception as e:
        return  HttpResponse(e)

def userRegister(request):
    try:
        return render(request, 'website/register.html')
    except Exception as e:
        return  HttpResponse(e)