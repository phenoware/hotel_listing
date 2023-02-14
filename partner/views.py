from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from .models import *
from hotels.models import *
from hotelsListingProj.decorators import check_vendor_account
from django.conf import settings
from django.core.mail import send_mail


# User Authentications
def partnerLogin(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password']

        if User.objects.filter(email = username).exists():
            user = authenticate(username= username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login Succeesfully')
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('/partner/')
            else:
                messages.success(request, 'Invalid Credentials')
                return redirect(request.GET.get('redirectUrl'))
            
        else:
            messages.success(request, 'Email address not exists with us.')
            return redirect(request.GET.get('redirectUrl'))

    else:
        return render(request, 'partner/partner-login.html')
    
def partnerLogout(request):
    logout(request)
    return redirect('/partner/')

def newRegistrations(request):
    try:
        if request.method == 'POST':
            
            name = request.POST['name'] 
            businessName = request.POST['businessName'] 
            password = request.POST['password']
            email = request.POST['email'] 
            phone = request.POST['phone'] 

            if User.objects.filter(email = email).exists():
                messages.success(request, 'Email Address is already registered with us.')
                return redirect(request.GET.get('redirectUrl'))
            else:
                # create user account here 
                user = User.objects.create_user(username= email, email= email, password= password)
                user.first_name = name
                user.save()

                if Partner.objects.filter(user_id = user.id).exists():
                    messages.success(request, 'Email Address is already registered with us.')
                    return redirect(request.GET.get('redirectUrl'))
                else:
                    Partner(user = user, phone = phone, businessName= businessName, password = password).save()

            # Login Partner In partner Panel 
            user = authenticate(username= email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login Succeesfully')
                return redirect('/partner/')
            else:
                messages.success(request, 'Invalid Login Credentials')
                return redirect(request.GET.get('redirectUrl'))


            

        else:
            return render(request, 'partner/partner-registrations.html')
    except Exception as e: 
        return HttpResponse(e)


@login_required(login_url='/partner/partner-login/')
@check_vendor_account()
def home(request):
    return render(request ,'partner/index.html')   

@login_required(login_url='/partner/partner-login/')
@check_vendor_account()
def bookings(request):
    try:
        return render(request, 'partner/bookings.html') 
    except Exception as e:
        return HttpResponse(e)

@login_required(login_url='/partner/partner-login/')
@check_vendor_account()
def bookingDetails(request):
    try:
        return render(request, 'partner/booking-details.html') 
    except Exception as e:
        return HttpResponse(e)


@login_required(login_url='/partner/partner-login/')
@check_vendor_account()
def hotels(request):
    try:
        properties = Property.objects.all().order_by('-id')
        params = {'properties':properties}

        return render(request, 'partner/hotels.html', params) 
    except Exception as e:
        return HttpResponse(e)

@login_required(login_url='/partner/partner-login/')
@check_vendor_account()
def AddNewHotel(request):
    try:
        facilities = Facilities.objects.all()
        params = {'facilities':facilities}
        if request.method == 'POST':
            
            vendor = Partner.objects.get(user_id = request.user.id)
            name = request.POST['name']
            propertyType = request.POST['propertyType']
            address = request.POST['address']
            city = request.POST['city']
            pincode = request.POST['pincode']
            overview = request.POST['overview']
            image = request.FILES['image']
            priceMin = request.POST['priceMin']

            property = Property(vendor = vendor, name= name, propertyType= propertyType, address= address, city= city, pincode = pincode, overview= overview, image= image, priceMin= priceMin)
            property.save()

            # check for facilities
            if request.FILES.getlist('images'):
                images = request.FILES.getlist('images')
                for i in images:
                    PropertyImages(property = property, image = i).save()
           


            if request.POST.getlist('facilities[]'):
                facilities = request.POST.getlist('facilities[]')
                for i in facilities:
                    facilitiesObj = Facilities.objects.get(id = i)
                    PropertyFacilities(property = property, facilities = facilitiesObj).save()

           
            messages.success(request, 'New property added')
            return redirect('/partner/hotels/')

            
        return render(request, 'partner/add-new-hotel.html', params)
    except Exception as e: 
        return HttpResponse(e)

@login_required(login_url='/partner/partner-login/')
@check_vendor_account()
def propertyDetails(request, slug):
    try:
        property = Property.objects.get(slug = slug)
        propertyImages = PropertyImages.objects.filter(property_id = property.id)
        roomsCount = Room.objects.filter(property_id = property.id).count()
        facilities = PropertyFacilities.objects.filter(property_id = property.id)
        rooms = Room.objects.filter(property_id = property.id)

        param = {'property':property, 'propertyImages':propertyImages, 'redirectUrl':request.GET.get('redirectUrl'), 'roomsCount':roomsCount, 'facilities':facilities, 'rooms':rooms}

        return render(request, 'partner/hotel-details.html', param) 
    except Exception as e:
        return HttpResponse(e)


@login_required(login_url='/partner/partner-login/')
@check_vendor_account()
def AddNewRoom(request, slug):
    try:
        property = Property.objects.get(slug = slug)
        if request.method == 'POST':
            name = request.POST['name'] 
            status = request.POST['status'] 
            roomType = request.POST['roomType'] 
            image = request.FILES['image'] 
            price = request.POST['price'] 
            adults = request.POST['adults'] 
            childrens = request.POST['childrens'] 
            redirectUrl = request.POST['redirectUrl']
            newRoom = Room(property= property, status = status, roomType= roomType, image=image, price =price, adults=adults, childrens=childrens,name =name)
            newRoom.save()
            # priceIncludes = request.POST['priceIncludes'] 


            if request.POST.getlist('facilities[]'):
                facilities = request.POST.getlist('facilities[]')
                for i in facilities:
                    roomFeatures = RoomFeatures.objects.get(id = i)
                    RoomPriceIncludes(room = newRoom, roomFeatures = roomFeatures).save()


            messages.success(request, 'New room added')
            return redirect(redirectUrl)
        else:
            redirectUrl = request.GET.get('redirectUrl')
            roomFeatures = RoomFeatures.objects.all()
            params = {'property':property, 'redirectUrl':redirectUrl, 'roomFeatures':roomFeatures}
        return render(request, 'partner/add-new-room.html', params)
    except Exception as e:
        return HttpResponse(e)


@login_required(login_url='/partner/partner-login/')
@check_vendor_account()
def deleteHotel(request, id):
    try:
        Property.objects.get(id = id).delete()
        messages.success(request,'Property Deleted')

        return redirect(request.GET.get('redirectUrl'))
    except Exception as e: 
        return HttpResponse(e) 


@login_required(login_url='/partner/partner-login/')
@check_vendor_account()
def vendorDetails(request):
    return render(request,'partner/vendor-details.html')