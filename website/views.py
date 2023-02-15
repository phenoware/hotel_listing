from django.shortcuts import render
from django.http import HttpResponse
from hotels.models import *

# Create your views here.

def home(request):
    try:
        property = Property.objects.all().order_by('-id')
        rooms = Room.objects.all().order_by('-id')

        params = {'property':property, 'rooms':rooms}
        return render(request, 'website/index.html', params)
    except Exception as e:
        return  HttpResponse(e)

def resorts(request):
    try:
        properties = Property.objects.all().order_by('-id')

        params = {'properties':properties}
        return render(request, 'website/hotels-listing.html', params)
    except Exception as e:
        return HttpResponse(e)


def hotelDetails(request, slug):
    try:
        property = Property.objects.get(slug = slug)
        images = PropertyImages.objects.filter(property_id = property.id)
        imagesCount = 1 + PropertyImages.objects.filter(property_id = property.id).count()
        propertyFacilities = PropertyFacilities.objects.filter(property_id = property.id)
        roomPriceIncludes = RoomPriceIncludes.objects.all()
        # Revere Data Access from foreign key
        rooms = property.propertyRooms.all()
        
        params = {'property':property, 'images':images, 'imagesCount':imagesCount, 'propertyFacilities':propertyFacilities, 'rooms':rooms, 'roomPriceIncludes':roomPriceIncludes}
        return render(request, 'website/hotel-details.html', params)
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